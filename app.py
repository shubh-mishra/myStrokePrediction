#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('strokePredict.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
  return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
  if request.method == 'POST':
      age = int(request.form['age'])
      marital_status=request.form['marital_status']
      work_type=request.form['work_type']
      heart_disease=request.form['heart_disease']
      hypertension=request.form['hypertension']
      smoke=request.form['smoke']
      
      if age>60:
          age_greater_60=1
      else:
          age_greater_60=0
      
      if hypertension == 'Yes':
          hypertension=1
      else:
          hypertension=0
          
      if heart_disease == 'Yes':
          heart_disease=1
      else:
          heart_disease=0
          
      if marital_status == 'Yes':
          ever_married_Yes=1
      else:
          ever_married_Yes=0
          
      if work_type == 'Private':
          work_type_Private=1
          work_type_Never_worked=0
          work_type_Self_employed=0
          work_type_children=0
      elif work_type == 'Self-employed':
          work_type_Private=0
          work_type_Never_worked=0
          work_type_Self_employed=1
          work_type_children=0
      elif work_type == 'Children':
          work_type_Private=0
          work_type_Never_worked=0
          work_type_Self_employed=0
          work_type_children=1
      elif work_type == 'Never worked':
          work_type_Private=0
          work_type_Never_worked=1
          work_type_Self_employed=0
          work_type_children=0
      else:
          work_type_Private=0
          work_type_Never_worked=0
          work_type_Self_employed=0
          work_type_children=0
          
      if smoke == 'Never smoked':
          smoking_status_formerly_smoked = 0
          smoking_status_never_smoked = 1
          smoking_status_smokes = 0
      elif smoke == 'Formerly smoked':
          smoking_status_formerly_smoked = 1
          smoking_status_never_smoked = 0
          smoking_status_smokes = 0
      elif smoke == 'Smokes':
          smoking_status_formerly_smoked = 0
          smoking_status_never_smoked = 0
          smoking_status_smokes = 1
      else:
          smoking_status_formerly_smoked = 0
          smoking_status_never_smoked = 0
          smoking_status_smokes = 0
          
      prediction=model.predict([[hypertension, heart_disease, age_greater_60, ever_married_Yes, work_type_Never_worked, work_type_Private, work_type_Self_employed, work_type_children, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]])
      
      if int(prediction)==1:
          return render_template('index.html',prediction_text="You are vulnerable to stroke. Please take good care of yourself!!")
      else:
          return render_template('index.html',prediction_text="You are safe from stroke. Enjoy!!")
  else:
      return render_template('index.html')

if __name__=="__main__":
  app.run(debug=True)

