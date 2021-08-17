import streamlit as st
from sklearn.preprocessing import StandardScaler
from PIL import Image
import pickle
import pandas as pd

# Title
st.header("AutoScout Car Price")
st.subheader("Select Car Features And Predict Price")


st.sidebar.header("Features Selection")
model = st.sidebar.radio('Select Car Model', ['A1','A3','Astra','Corsa','Insignia','Clio','Espace'])
gearing_type = st.sidebar.radio('Select Gearing Type', ["Automatic","Semi-Auto","Manuel"])
hp = st.sidebar.slider("Power Of The Car (hp)",1,500)
km = st.sidebar.slider("Mileage Of The Car (km)",0,250000)
age = st.sidebar.slider("Age Of The Car (year)",0,50)

if model == "A1":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\A1_1.jpg")
    st.image(img, caption=f"{model}")
elif model == "A3":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\A3_1.jpg")
    st.image(img, caption=f"{model}")
elif model == "Astra":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Astra_1.jpg")
    st.image(img, caption=f"{model}")
elif model == "Clio":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Clio_1.jpg")
    st.image(img, caption=f"{model}")
elif model == "Corsa":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Corsa_1.jpg")
    st.image(img, caption=f"{model}")
elif model == "Espace":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Espace_1.jpg")
    st.image(img, caption=f"{model}")
elif model == "Insignia":
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\Insignia_1.jpg")
    st.image(img, caption=f"{model}")
else:
    img = Image.open("D:\Data Scientist\Data Science\ML-Deployment\Project\AutoScout Deployment\All.jpg")
    st.image(img, caption=f"{model}")




# Model Load
model=pickle.load(open("lasso_final_model", "rb"))

# Scale Load
scaler=pickle.load(open("scaler", "rb"))

# Columns Load
X_columns = pickle.load(open("colums", "rb"))

# Data
my_dict = {
    "hp": hp,
    "age": age,
    "km": km,
    "model": model,
    "gearing_type": gearing_type
}

# DataDrame
my_dict_1 = pd.DataFrame([my_dict])

# Dummies
my_dict_2 = pd.get_dummies(my_dict_1).reindex(columns=X_columns, fill_value=0)

#st.table(my_dict_2)

# Scale
my_dict_3 = scaler.transform(my_dict_2)

# Predict
pred_result = model.predict(my_dict_3)

#st.subheader("Press Predict")
if st.button("Predict"):
    prediction = pred_result
    st.success("The Car Price Prediction is ${}. ".format(int(prediction)))