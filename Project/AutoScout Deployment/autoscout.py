import streamlit as st
import pickle
import pandas as pd

# Title
st.header("AutoScout Car Price")
st.subheader("Select Car Features And Predict Price")
#from PIL import Image
#img = Image.open("Machine Learning.jpg")
#st.image(img, width=200, caption="my_image")




st.sidebar.success("Features Selection")
model = st.sidebar.radio('Select Car Model', ['A1','A3','Astra','Corsa','Insignia','Clio','Espace'])
gearing_type = st.sidebar.radio('Select Gearing Type', ["Automatic","Semi-Auto","Manuel"])
hp = st.sidebar.slider("Power Of The Car (hp)",1,1000)
km = st.sidebar.slider("Mileage Of The Car (km)",0,2000000)
age = st.sidebar.slider("Age Of The Car (year)",0,100)

# Model
model=pickle.load(open("lasso_final_model", "rb"))

# Data
my_dict = {
    "hp": hp,
    "age": age,
    "km": km,
    "model": model,
    "gearing_type": gearing_type
}

# DataDrame
my_dict = pd.DataFrame([my_dict])
my_dict

my_dict = pd.get_dummies(my_dict).reindex(columns=X.columns, fill_value=0)
my_dict

# Scale
my_dict = scaler.transform(my_dict)

model.predict(my_dict)