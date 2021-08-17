import streamlit as st
from sklearn.preprocessing import StandardScaler
from PIL import Image
import pickle
import pandas as pd

# Title
st.header("AutoScout Car Price")
st.subheader("Select Car Features And Predict Price")


st.sidebar.header("Features Selection")
model_1 = st.sidebar.radio('Select Car Model', ['A1','A3','Astra','Clio','Corsa','Espace','Insignia'])
gearing_type = st.sidebar.radio('Select Gearing Type', ["Automatic","Semi-automatic","Manual"])
hp = st.sidebar.slider("Power Of The Car (hp)",1,500)
km = st.sidebar.slider("Mileage Of The Car (km)",0,250000)
age = st.sidebar.slider("Age Of The Car (year)",0,50)

if model_1 == "A1":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\A1_1.jpg")
    st.image(img, caption=f"{model_1}")
elif model_1 == "A3":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\A3_1.jpg")
    st.image(img, caption=f"{model_1}")
elif model_1 == "Astra":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Astra_1.jpg")
    st.image(img, caption=f"{model_1}")
elif model_1 == "Clio":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Clio_1.jpg")
    st.image(img, caption=f"{model_1}")
elif model_1 == "Corsa":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Corsa_1.jpg")
    st.image(img, caption=f"{model_1}")
elif model_1 == "Espace":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Espace_1.jpg")
    st.image(img, caption=f"{model_1}")
elif model_1 == "Insignia":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Insignia_1.jpg")
    st.image(img, caption=f"{model_1}")
else:
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\All.jpg")
    st.image(img, caption=f"{model_1}")


# Model Load
model=pickle.load(open("lasso_final_model", "rb"))

# Scale Load
scaler=pickle.load(open("scaler", "rb"))

# Columns Load
X_columns = pickle.load(open("colums", "rb"))

# Data
my_dict = { 
    "model": model_1,
    "gearing_type": gearing_type,   
    "hp": hp,
    "age": age,
    "km": km       
}

# DataDrame
my_dict_1 = pd.DataFrame([my_dict])

# Dummies
my_dict_2 = pd.get_dummies(my_dict_1).reindex(columns=X_columns, fill_value=0)

#st.table(my_dict_2) ######

# Scale
my_dict_3 = scaler.transform(my_dict_2)

# Predict
pred_result = model.predict(my_dict_3)

# Config
st.dataframe(my_dict_1)

#st.subheader("Press Predict")
if st.button("Predict"):
    prediction = pred_result
    st.success("The Car Price Prediction is ${}. ".format(int(prediction)))