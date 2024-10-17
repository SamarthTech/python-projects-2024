import torch
from torch import nn, optim
from torch.utils import data

from utils import *
import pandas as pd
import numpy as np
from os import makedirs
from typing import Union
import matplotlib.pyplot as plt
from dataclasses import dataclass

import warnings
warnings.filterwarnings('ignore')


class MnistModel(nn.Module):
    """
    Custom CNN Model for Mnist
    """

    def __init__(self, classes: int) -> None:
        super(MnistModel, self).__init__()

        self.classes = classes

        # initialize the layers in the first (CONV => RELU) * 2 => POOL + DROP
        # (N,1,28,28) -> (N,16,24,24)
        self.conv1A = nn.Conv2d(
            in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=0)
        # (N,16,24,24) -> (N,32,20,20)
        self.conv1B = nn.Conv2d(
            in_channels=16, out_channels=32, kernel_size=5, stride=1, padding=0)
        # (N,32,20,20) -> (N,32,10,10)
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        self.act = nn.ReLU()
        self.do = nn.Dropout(0.25)

        # initialize the layers in the second (CONV => RELU) * 2 => POOL + DROP
        # (N,32,10,10) -> (N,64,8,8)
        self.conv2A = nn.Conv2d(
            in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0)
        # (N,64,8,8) -> (N,128,6,6)
        self.conv2B = nn.Conv2d(
            in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)
        # (N,128,6,6) -> (N,128,3,3)
        self.pool2 = nn.MaxPool2d(kernel_size=2)

        # initialize the layers in our fully-connected layer set
        # (N,128,3,3) -> (N,32)
        self.dense3 = nn.Linear(128*3*3, 32)

        # initialize the layers in the softmax classifier layer set
        # (N, classes)
        self.dense4 = nn.Linear(32, self.classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:

        # build the first (CONV => RELU) * 2 => POOL layer set
        x = self.conv1A(x)
        x = self.act(x)
        x = self.conv1B(x)
        x = self.act(x)
        x = self.pool1(x)
        x = self.do(x)

        # build the second (CONV => RELU) * 2 => POOL layer set
        x = self.conv2A(x)
        x = self.act(x)
        x = self.conv2B(x)
        x = self.act(x)
        x = self.pool2(x)
        x = self.do(x)

        # build our FC layer set
        x = x.view(x.size(0), -1)
        x = self.dense3(x)
        x = self.act(x)
        x = self.do(x)

        # build the softmax classifier
        x = nn.functional.log_softmax(self.dense4(x), dim=1)

        return x


class MnistDataset(data.Dataset):
    """
    Custom Dataset for Mnist
    """

    def __init__(self, df: pd.DataFrame, target: np.array, test: bool = False) -> None:
        self.df = df
        self.test = test

        # if test=True skip this step
        if not self.test:
            self.df_targets = target

    def __len__(self) -> int:
        # return length of the dataset
        return len(self.df)

    def __getitem__(self, idx: int) -> Union[tuple, torch.Tensor]:
        # if indexes are in tensor, convert to list
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # if test=False return bunch of images, targets
        if not self.test:
            return torch.as_tensor(self.df[idx].astype(float)), self.df_targets[idx]
        # if test=True return only images
        else:
            return torch.as_tensor(self.df[idx].astype(float))


def loss_fn(outputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """
    Loss Function

    Args:
        outputs (torch.Tensor): Predicted Labels
        targets (torch.Tensor): True Labels

    Returns:
        torch.Tensor: NLLLoss value
    """
    return nn.NLLLoss()(outputs, targets)


def train_loop_fn(data_loader, model, optimizer, device, scheduler=None):
    """
    Training Loop

    Args:
        data_loader: Train Data Loader
        model: NN Model
        optimizer: Optimizer
        device: Device (CPU/CUDA)
        scheduler: Scheduler. Defaults to None.
    """
    # set model to train
    model.train()
    # iterate over data loader
    train_loss = []
    for ids, targets in data_loader:
        # sending to device (cpu/gpu)
        ids = ids.to(device, dtype=torch.float)
        targets = targets.to(device, dtype=torch.long)

        # Clear gradients w.r.t. parameters
        optimizer.zero_grad()
        # Forward pass to get output/logits
        outputs = model(x=ids)
        # Calculate Loss: softmax --> negative log likelihood loss
        loss = loss_fn(outputs, targets)
        train_loss.append(loss)
        # Getting gradients w.r.t. parameters
        loss.backward()
        optimizer.step()

        if scheduler is not None:
            # Updating scheduler
            if type(scheduler).__name__ == 'ReduceLROnPlateau':
                scheduler.step(loss)
            else:
                scheduler.step()
    print(f"Loss on Train Data : {sum(train_loss)/len(train_loss)}")


def eval_loop_fn(data_loader, model, device):
    """
    Evaluation Loop

    Args:
        data_loader: Evaluation Data Loader
        model: NN Model
        device: Device (CPU/CUDA)

    Returns:
        List of Target Labels and True Labels
    """
    # full list of targets, outputs
    fin_targets = []
    fin_outputs = []
    # set model to eveluate
    model.eval()  # as model is set to eval, there will be no optimizer and scheduler update

    # iterate over data loader
    for _, (ids, targets) in enumerate(data_loader):
        ids = ids.to(device, dtype=torch.float)
        targets = targets.to(device, dtype=torch.long)

        outputs = model(x=ids)
        loss = loss_fn(outputs, targets)
        loss.backward()

        # Get predictions from the maximum value
        _, outputs = torch.max(outputs.data, 1)

        # appending the values to final lists
        fin_targets.append(targets.cpu().detach().numpy())
        fin_outputs.append(outputs.cpu().detach().numpy())
    return np.vstack(fin_outputs), np.vstack(fin_targets)


def test_loop_fn(test, model, device):
    """
    Testing Loop

    Args:
        test: Test DataFrame
        model: NN Model
        device: Device (CPU/CUDA)

    Returns:
        List of Predicted Labels
    """
    model.eval()
    # convert test data to FloatTensor
    test = torch.as_tensor(test)
    test = test.to(device, dtype=torch.float)

    # Get predictions
    pred = model(test)
    # Get predictions from the maximum value
    _, predlabel = torch.max(pred.data, 1)
    # converting to list
    predlabel = predlabel.tolist()

    # Plotting the predicted results
    L = 5
    W = 5
    _, axes = plt.subplots(L, W, figsize=(12, 12))
    axes = axes.ravel()

    for i in np.arange(0, L * W):
        axes[i].imshow(test[i].cpu().detach().numpy().reshape(28, 28))
        axes[i].set_title("Prediction Class = {:0.1f}".format(predlabel[i]))
        axes[i].axis('off')

    plt.suptitle('Predictions on Test Data')
    plt.subplots_adjust(wspace=0.5)
    plt.show()

    return predlabel


@timer
def run(args):
    """
    Function where all the magic happens

    Args:
        args: Arguments for Training

    Returns:
        List of Predicted Labels
    """
    # reading train and test data
    print('Reading Data..')
    dfx = pd.read_csv(args.data_path+'train.csv')
    df_test = pd.read_csv(args.data_path+'test.csv')

    classes = dfx[args.target].nunique()

    print('Data Wrangling..')
    # spliting train data to train, validate
    split_idx = int(len(dfx) * 0.8)
    df_train = dfx[:split_idx].reset_index(drop=True)
    df_valid = dfx[split_idx:].reset_index(drop=True)

    # target labels
    train_targets = df_train[args.target].values
    valid_targets = df_valid[args.target].values

    # reshaping data to 28 x 28 images and normalize
    df_train = df_train.drop(args.target, axis=1).values.reshape(
        len(df_train), 1, 28, 28)/255
    df_valid = df_valid.drop(args.target, axis=1).values.reshape(
        len(df_valid), 1, 28, 28)/255
    df_test = df_test.values.reshape(len(df_test), 1, 28, 28)/255

    print('DataSet and DataLoader..')
    # Creating PyTorch Custom Datasets
    train_dataset = MnistDataset(df=df_train, target=train_targets)
    valid_dataset = MnistDataset(df=df_valid, target=valid_targets)

    # Creating PyTorch DataLoaders
    train_data_loader = data.DataLoader(
        dataset=train_dataset, batch_size=args.BATCH_SIZE, shuffle=True)
    valid_data_loader = data.DataLoader(
        dataset=valid_dataset, batch_size=args.BATCH_SIZE, shuffle=False)

    # device (cpu/gpu)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # instatiate model and sending it to device
    model = MnistModel(classes=classes).to(device)
    # instantiate optimizer
    optimizer = optim.SGD(model.parameters(), lr=args.lr)
    # instantiate scheduler
    scheduler = optim.lr_scheduler.CyclicLR(
        optimizer, base_lr=args.lr, max_lr=0.1)

    print('Training..')
    best_accuracy = 0
    # loop through epochs
    for epoch in range(args.NUM_EPOCHS):
        print(f'Epoch [{epoch+1}/{args.NUM_EPOCHS}]')
        # train on train data
        train_loop_fn(train_data_loader, model, optimizer, device, scheduler)
        # evaluate on validation data
        o, t = eval_loop_fn(valid_data_loader, model, device)
        accuracy = (o == t).mean() * 100
        print(f'Accuracy on Valid Data : {accuracy} %')
        if accuracy > best_accuracy:
            torch.save(model.state_dict(), args.model_path)
            best_accuracy = accuracy

    # Predict on test data
    return test_loop_fn(df_test, model, device)


if __name__ == "__main__":
    # variables for training model
    @dataclass
    class Args:
        lr: float = 3e-5
        RANDOM_STATE: int = 42
        NUM_EPOCHS: int = 5
        BATCH_SIZE: int = 100
        target: str = 'label'
        data_path: str = 'data/'
        model_path: str = 'checkpoint/mnist.pt'

        def __post_init__(self):
            makedirs('checkpoint', exist_ok=True)

    arg = Args()
    random_seed(arg.RANDOM_STATE)
    test_preds = run(args=arg)
