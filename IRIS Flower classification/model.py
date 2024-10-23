import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from joblib import dump, load
sns.set()

##################### LOAD THE DATA #############################
df = pd.read_csv('iris-with-answers.csv')
df1 = pd.read_csv('iris-with-answers.csv')
df

df['species'] = df.species.map({'setosa':0,'virginica':1,'versicolor':2})
df

################### VISUALIZATION #############################
df.corr()

fig = plt.figure(figsize=(12,10))

ax1=plt.subplot(221)
ax1.scatter(df.sepal_length,df.petal_length)
plt.xlabel('sepal_length')
plt.ylabel('petal_length')

ax2=plt.subplot(222)
ax2.scatter(df.petal_width,df.petal_length)
plt.xlabel('petal_width')
plt.ylabel('petal_length')

#from sklearn.preprocessing import MinMaxScaler

#scaler = MinMaxScaler()
#X_normalised = scaler.fit_transform(df)

#x_s = pd.DataFrame({'sl': X_normalised[:, 0], 'sw': X_normalised[:, 1], 'pl': X_normalised[:, 2], 'pw': X_normalised[:, 3], 'species': X_normalised[:, 4]})
#x_s.reset_index(drop=True,inplace=True)
#x_s

#X = x_s.iloc[:,:4]
#y = x_s.iloc[:,[4]]
#X,y

####################### TRAIN,TEST SPLIT ########################

X = df.iloc[:,:4]
y = df.iloc[:,[4]]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
X_train
X_test
y_train



####################### MODELING ################################
from sklearn.tree import DecisionTreeRegressor

DT = DecisionTreeRegressor(max_depth=4)
DT.fit(X_train,y_train)
DT.score(X_train, y_train)
DT.score(X_test, y_test)
y_test_pred = DT.predict(X_test)

X_test,y_test

####################### INPUT TEST ###############################
import numpy as np

sl = float(input('enter sepal len :'))
sw = float(input('enter sepal wid :'))
pl = float(input('enter petal len :'))
pw = float(input('enter petal wid :'))

value = np.array([[sl,sw,pl,pw]])
#value_df = pd.DataFrame({'sl': value[:, 0], 'sw': value[:, 1], 'pl': value[:, 2], 'pw':value[:, 3]})
#val_scaled = scaler.fit_transform(np.float32(value))
#v = np.array(val_scaled).T
output = np.round(DT.predict(value,1))


#print(output,type(output))

if output == 0:
    print('Setosa')
elif output == 1:
    print('Virginica')
elif output == 2:
    print('Versicolor')


############## SAVE THE MODEL AS A PRECOMPILED PKL FILE ##################
pickle.dump(DT, open('model.pkl', 'wb'))  


