import pickle
import streamlit as st
from streamlit_option_menu import option_menu

health_insurance_model=pickle.load(open('health_insurance_model','rb'))

with st.sidebar:
    selected=option_menu('health_insurance_cost_prediction,icons=['heart'],default_index=0)
    
    
    
if(selected=='health_insurance_model'):
    st.title('predict premiun of your health insurance')
    
    col1,col2 = st.column(2)
    
    with col1:
        age = st.text_input('current age')
        
    with col2:
        sex =st.text_input('enter gender  1|0: female-0 , male-1')
        
    with col1:
        bmi =st.text_input('BMI rate')
        
    with col2:
        smoker =st.text_input('enter smoker 1|0: NO-0,YES-1')
        
        
    health_diagonsis=''
    
    if st.button(test_result):
        health_prediction = health_predict([[age,sex,bmi,smoker]])
        
        if(health_prediction[0] ==1):
            health_diagonsis="your premium prediction"
            
        else:
            health_diagonsis="input is not appropriate"
            
    st.success(health_diagonsis)
    