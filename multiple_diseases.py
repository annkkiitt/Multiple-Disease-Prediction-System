# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved model 
diabetes_model = pickle.load(open('diabetes.sav','rb'))
heart_model = pickle.load(open('heart_disease.sav','rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction','Heart Disease Prediction'],
                           icons=['activity','heart-pulse']
                           ,default_index=0)
    
if(selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction')
    
    col1,col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
        
    with col2:
        Glucose	= st.text_input('Glucose Level') 

    with col1:
        BloodPressure = st.text_input('Blood pressure level')

    with col2:
        SkinThickness = st.text_input('Skin thickness value')
    
    with col1:
        Insulin	= st.text_input('Insulin level')
      
    with col2:
        BMI	= st.text_input('BMI value')
      
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function value')
    
    with col2:
        Age	= st.text_input('Age of person')
    
    diabetes_result = ''
    
    #button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if(diabetes_prediction[0] == 1):
            diabetes_result = 'Person is diabetic'
        else:
            diabetes_result = 'Person is non diabetic'
            
    st.success(diabetes_result)
        
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of person')
        
    with col2:
        sex = st.text_input('Sex : Male-1, Female-0')
        
    with col3:
        cp = st.text_input('chest pain type (4 values)')
        
    with col1:
        trestbps = st.text_input('Resting blood pressure')
        
    with col2:
        chol = st.text_input('Cholestoral in mg/dl')
    
    with col3:
        fbs = st.text_input('Fasting blood sugar > 120 mg/dl')
    
    with col1:
        restecg = st.text_input('Resting electrocardiographic results (values 0,1,2)')
        
    with col2:
        thalach = st.text_input('Maximum heart rate')
        
    with col3:
        exang = st.text_input('Exercise induced angina')
        
    with col1:
        oldpeak = st.text_input('Old peak')
        
    with col2:
        slope = st.text_input('The slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels (0-3) colored by flourosopy')
        
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    heart_disease_result = ''
    
    if st.button('Heart Disease Result'):
        if age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal:
            # Perform type conversion only if all input fields are non-empty
            age = int(age)
            sex = int(sex)
            cp = int(cp)
            trestbps = int(trestbps)
            chol = int(chol)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = int(thalach)
            exang = int(exang)
            oldpeak = float(oldpeak)
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)
            
        heart_disease_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if(heart_disease_prediction[0]==1):
            heart_disease_result = 'Person have heart disease'
        else:
            heart_disease_result = 'Person does not have heart disease'
    
    st.success(heart_disease_result)
    
    

