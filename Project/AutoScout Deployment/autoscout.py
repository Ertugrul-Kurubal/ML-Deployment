import streamlit as st
import pickle
import pandas as pd

# Title
st.header("AutoScout Car Price")

st.subheader("Select Car Features And Predict Price")



st.sidebar.success("Features Selection")
st.sidebar.radio('Select Car Brand', ["Audi","BMW","Mercedes"])