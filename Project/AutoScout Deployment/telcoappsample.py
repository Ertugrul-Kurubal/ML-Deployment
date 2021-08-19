import streamlit as st
import pickle
import pandas as pd

st.sidebar.title('Telco Churn Prediction')

tenure=st.sidebar.slider("How long in months:",1,99,step=1)
MonthlyCharges=st.sidebar.slider("What is MonthlyCharge", 18, 200, step=5)
TotalCharges=st.sidebar.slider("What is TotalCharge", 18, 8684, step=18)
InternetService=st.sidebar.selectbox("What is the type of your service", ('Fiber optic','DSL','No'))
OnlineSecurity=st.sidebar.radio ("Do you have online security", ('Yes','No'))
TechSupport=st.sidebar.radio ("Do you have techsupport", ('Yes','No'))
Contract=st.sidebar.selectbox("What is the type of contract", ('Month-to-month','Two year','One year')) 

model_name=st.selectbox("Select your model:",("LogReg","RandomForest"))
if model_name=="LogReg":
	model=pickle.load(open("model_logreg","rb"))
	st.success("You selected {} model".format(model_name))
else:
	model=pickle.load(open("model_ranfor","rb"))
	st.success("You selected {} model".format(model_name))


my_dict = {
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "InternetService": InternetService,
    "OnlineSecurity":OnlineSecurity,
    "TechSupport":TechSupport,
    "Contract":Contract

}

df = pd.DataFrame.from_dict([my_dict])

columns=['tenure', 'MonthlyCharges', 'TotalCharges',
       'InternetService_Fiber optic', 'InternetService_No',
       'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
       'TechSupport_No internet service', 'TechSupport_Yes',
       'Contract_One year', 'Contract_Two year']

df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)


st.header("The configuration is below")
st.table(df)

st.subheader("Press predict if configuration is okay")
if st.button("Predict"):
    prediction=model.predict(df)
    st.success("The churn prediction is {}. ".format(int(prediction)))

