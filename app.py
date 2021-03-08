import streamlit as st
import numpy as np
from sklearn.svm import SVC
from pickle import dump,load

col1 = st.text_input("col1","type here")
col2 = st.text_input("col2","type here")
classifier = load(open('model.pkl','rb'))

input = np.array([[col1,col2]]).astype(np.float64)
prediction = classifier.predict(input)
if st.button("Predict"):
    st.success(prediction)    