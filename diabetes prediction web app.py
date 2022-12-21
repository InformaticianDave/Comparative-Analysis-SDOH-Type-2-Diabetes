import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

loaded_model = pickle.load(open('C:/Users/Professor Liu/Desktop/Python Portfolio/Machine Learning Tableau Projects/Streamlit Deployments/trained_model.pkl', 'rb'))
#funtion for prediciton
"""
Data Dictionary:
Age = (13-level age category)

1 = 18 - 24

2 = 25 - 29	

3 = 30 - 34	

4 = 35 - 39	

5 = 40 - 44	

6 = 45 - 49	

7 = 50 - 54	

8 = 55 - 59	

9 = 60 - 64	

10 = 65 - 69	

11 = 70 - 74	

12 = 75 - 79	

13 = 80+

Education = (Education level)

1 = Never attended school or only kindergarten	

2 = Grades 1-8 (Elementary)	

3 = Grades 9 -11 (Some high school)	

4 = Grades 12 or GED (High school graduate)

5 = College 1-3 years (Some college or technical school)

6 = College 4 years or more (College graduate)


Income = (Income Level)

1 = Less than $10,000

2 = $10,000 - $15,000

3 = $15,000 - $20,000

4 = $20,000 - $25,000

5 = $25,000 - $35,000

6 = $35,000 - $50,000

7 = $50,000 - $75,000

8 = $75,000+

    """

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    elif (prediction[1] == 1):
        return 'The person is diabetic'
    else:
        return 'The values you input are incorrect check again'

def main():
    
    
    # giving a title
    st.title('Social Determinants of Health Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    AnyHealthcare = st.number_input('Do you have healthcare insurance? 0 for No or 1 for Yes')
    NoDocbcCost = st.number_input('Do you have a primary doctor? 0 for No or 1 for Yes')
    Sex = st.number_input('What is your sex? 0 for female or 1 for male')
    Age = st.number_input('Enter your age group value (refer to data dictionary)')
    Education = st.number_input('Enter your education group value (refer to data dictionary)')
    Income = st.number_input('Enter your income group value (refer to data dictonary)')
    
    
    # code for Prediction
    Social_determinants = ''
    
    # creating a button for Prediction
    submit = st.button('Predict')
    if submit:
        Social_determinants = diabetes_prediction([AnyHealthcare, NoDocbcCost, Sex, Age, Education, Income])
        if Social_determinants == 0:
            st.write('Based on your social determinants of health:')
        else:
            st.write('Based on your social determinants of health:')
        
    st.success(Social_determinants)
    
    
if __name__ == '__main__':
    main()

