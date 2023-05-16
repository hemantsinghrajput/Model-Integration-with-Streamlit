import streamlit as st
import numpy as np
import pickle
from PIL import Image

scaler = pickle.load(open('C://Users//HP//Desktop//Mlops//one2//models//standard_scaler.pkl', 'rb'))
lr_model = pickle.load(open('C://Users//HP//Desktop//Mlops//one2//models//lr_model.pkl', 'rb'))

image = Image.open('C://Users//HP//Desktop//Mlops//one2//integration//img//wine.jpg')

st.image(image, caption='Wine Quality')

va = st.number_input('Enter the volatile acidity: ')
ca = st.number_input('Enter the citric acid: ')
sd = st.number_input('Enter the total sulfur dioxide: ')
su = st.number_input('Enter the sulphates: ')
al = st.number_input('Enter the alcohol: ')

btn_click = st.button("Predict")

if btn_click:
    if va and ca and sd and su and al:
        query_point = np.array([va, ca, sd, su, al]).reshape(1, -1)
        query_point_transformed = scaler.transform(query_point)
        pred = lr_model.predict(query_point_transformed)
        st.success(pred[0])
    else:
        st.error("Enter the values properly.")
