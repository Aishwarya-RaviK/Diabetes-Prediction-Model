#Importing neccessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import pickle 
from sklearn.linear_model import LogisticRegression

#Loading the model
pickle_file=open("diabetes_prediction.pkl","rb")
classifier=pickle.load(pickle_file)

#Function for the prediction
def prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    prediction=classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    return prediction

def main():
    st.title('Diabetes Prediction')
    from PIL import Image 
    image=Image.open('background.jpg')
    st.image(image,caption='Diabetes Prediction')
    st.header('Give us the following information')

#The data to be provided
    Pregnancies=st.number_input('Pregnanices')
    Glucose=st.number_input('Glucose')
    BloodPressure=st.number_input('BloodPressure')
    SkinThickness=st.number_input('SkinThickness')
    Insulin=st.number_input('Insulin')
    BMI=st.number_input('BMI')
    DiabetesPedigreeFunction=st.number_input('DiabetesPedigreeFunction')
    Age=st.number_input('Age')


#Button to predict
    if st.button("Check"):
        result=prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        st.write('Your result')
        if result==[0]:
            result='Negative'
        else:
            result='Positive'
        st.success(result)
if __name__=='__main__':
    main()