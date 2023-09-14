# Apply FLASK FOR Heart Disease Prediction UI
from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

app= Flask(__name__)
#Load model
model =pickle.load(open(r'C:\Users\Flower#\Downloads\Jupfolder\Final_Project\model.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    health =int(request.form['General_Health'])
    exercise=int(request.form['Exercise'])
    diabetes=int(request.form['Diabetes'])
    arthritis=int(request.form['Arthritis'])
    age=int(request.form['Age_Category'])
    bmi=float(request.form['BMI'])
    smoking=int(request.form['Smoking_History'])
    female=int(request.form['Sex_Female'])
    male=int(request.form['Sex_Male'])
    
    # Scaling input
    scaler = StandardScaler()
    X_input = np.array([health, exercise,diabetes,arthritis,age,bmi,smoking,female,male])
    X_inputreshape = X_input.reshape(-1,1)
    input_data = scaler.fit_transform(X_inputreshape)
    list=input_data.reshape(1,-1)

    result = model.predict(list)[0]
    if (result==1):
        resultstr = 'Has Heart Disease'
    else:
        resultstr = 'No Heart Disease'
    
    return f'Prediction:  {resultstr}'



if __name__=='__main__':
    app.run(debug=True)
