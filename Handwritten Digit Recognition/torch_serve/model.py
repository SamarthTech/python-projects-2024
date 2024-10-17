import torch
from torch import nn


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
