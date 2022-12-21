import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Professor Liu/Desktop/Python Portfolio/Machine Learning Tableau Projects/Streamlit Deployments/trained_model.pkl', 'rb'))

input_data = (1,0,0,9,5,1)
# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
elif (prediction[1] == 1):
    print('The person is diabetic')
else:
    print('The values you input are incorrect check again')