import pickle
import numpy as np


model = pickle.load(open('model.pkl','rb'))


inputs = np.array([6.5,3.2,5.1,2]).reshape(1,4)
output = model.predict(inputs)
