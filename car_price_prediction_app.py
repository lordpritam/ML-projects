import streamlit as st
import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import joblib
from sklearn.ensemble import GradientBoostingRegressor


def main():
    html_temp ="""
     <div style = "background-color:lightblue;padding:16px">
     <h2 style="color:black;text-align:center;"> Car Price Prediction Using ML</h2>
     </div>
    """
    model = GradientBoostingRegressor()
    model = joblib.load('car_price_predictor')
    
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
     
    st.markdown("#### Are you planning to sell your car?\n#### So let's try evaluating the price.")
    
    p1 = st.number_input("What is the Current ex-showroom price(In Lakhs)",2.5,500.0,step=1.0)
    p2 = st.number_input("How many Kilometers car has Driven?",0,500000, step =100)
    
    s1 = st.selectbox("Fuel Type",('Petrol','Diesel','CNG'))
    if s1 == "Petrol":
        p3=0
    elif s1 == 'Diesel':
        p3=1
    elif s1 == 'CNG':
        p3=2
        
    s2 = st.selectbox("Seller Type",('Dealer','Individual'))
    if s2 == "Dealer":
        p4=0
    elif s1 == 'Individual':
        p4=1
    
    s3 = st.selectbox("Transmission Type",('Manual','Automatic'))
    if s3 == "Manual":
        p5=0
    elif s1 == 'Automatic':
        p5=1   
    
    p6 = st.slider("Number of owners the car previously had?",0,3)
    
    date_time = datetime.datetime.now()
    
    years = st.number_input("In Which Year Car Was Purchased?",1990,date_time.year)
    
    p7 = date_time.year - years
    
    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    
    
    if st.button('Predict'):
        pred = model.predict(data_new)
        st.success('You can sell your car for {} Lakhs'.format(pred[0]))
    
    
if __name__ == '__main__':
    main()
