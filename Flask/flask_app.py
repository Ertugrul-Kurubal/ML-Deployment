from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/api", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        my_dict = {
        "hp": request.form["hp"],
        "age": request.form["age"],
        "km": request.form["km"],
        "model": request.form["model"],
        "gearing_type": request.form["gearing_type"],
        "fuel": request.form["fuel"],
        "body_color":request.form["body_color"]
        }
        my_dict = pd.DataFrame([my_dict])
        my_dict = pd.get_dummies(my_dict).reindex(columns=loaded_columns, fill_value=0)
        my_dict = loaded_scaler.transform(my_dict)
        loaded_model.predict(my_dict)    
        return "post method"
    else:
        return "get method"

if __name__ == "__main__":
    loaded_model = joblib.load(open("d_final_model","rb"))
    loaded_scaler = joblib.load(open("d_scaler","rb"))
    loaded_columns = joblib.load(open("d_columns","rb"))
    app.run(debug=True, port=80, host="0.0.0.0")