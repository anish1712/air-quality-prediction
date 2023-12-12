import streamlit as st
import joblib 
import numpy as np
model = joblib.load('Air_Quality_Prediction.pkl')

def predict(input_data):
    pre= model.predict(input_data)
    return pre
st.title('Air_Quality_Prediction')
PM = st.number_input('enter PM2.5:')
NO = st.number_input('enter NO:')
NOx = st.number_input('enter NOx:')
CO = st.number_input('enter CO:')
NO2 = st.number_input('enter NO2:')
SO2 = st.number_input('enter SO2:')
O3 = st.number_input('enter O3:')
NO_NO2_Interaction = NO * NO2
NO2_NOx_Interaction = NO2 * NOx
CO_SO2_Interaction = CO * SO2

arr=np.array([[PM, NO, NOx, CO, NO2, SO2, O3, NO_NO2_Interaction, NO2_NOx_Interaction, CO_SO2_Interaction]])

if st.button("pridict"):
    result= predict(arr)
    st.success(f'AQI = {result}')




