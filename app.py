import pickle as pkl 
import streamlit as st

model = pkl.load(open("model.pkl","rb+"))
sc = pkl.load(open("scaler.pkl","rb+"))
st.title("Diabetic Patient Prediction Project")
gender = st.selectbox("Enter gender",["Male","Female","Other"])
if gender=='Female':
    gender=0
elif gender=='Male':
    gender=1
else:
    gender=2
age = st.number_input("Enter age",min_value=5,max_value=100)

hypertension = st.selectbox("Enter hypertension",["No","Yes"])

if hypertension=="No":
    hypertension=0
else:
    hypertension=1

heart_disease = st.selectbox("Enter heart disease",["No","Yes"])

if heart_disease=="No":
    heart_disease=0
else:
    heart_disease=1

smoking_history = st.selectbox("Enter smoking history",['never', 'No Info', 'current', 'former', 'ever', 'not current'])
if smoking_history=='never':
    smoking_history=0
elif smoking_history=='former':
    smoking_history=1
elif smoking_history=='not current':
    smoking_history=2
elif smoking_history=='current':
    smoking_history=3
elif smoking_history=='ever':
    smoking_history=2
else:
    smoking_history=-1
bmi = st.number_input("Enter bmi")
HbA1c_level = st.number_input("Enter HbA1c_level")
blood_glucose_level = st.number_input("Enter blood_glucose_level")
if st.button("Predict"):
    
    result = model.predict(sc.transform([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]]))
    result = result[0]
    if result == 1:
        st.error("Person is diabetic")
    else:
        st.success("Person is not diabetic")
