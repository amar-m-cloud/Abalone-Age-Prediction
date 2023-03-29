import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib


app = Flask(__name__) #Initialize the flask App

model = joblib.load('abalone.pkl')

@app.route('/')
def home():
    return render_template('weblone.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    inp_features = [[x for x in request.form.values()]]

    x_cols = ['Gender','Length','Diameter','Height','Whole Weight','Shucked Weight','Viscera Weight','Shell Weight']

    inputdata = pd.DataFrame(inp_features, columns = x_cols)

    prediction = model.predict(inputdata)

    output = round(prediction[0], 0)

    return render_template('weblone.html', Text = "For The Given Abalone Dimensions: ",Rings = "Number of Rings: {} ".format(output), Age = "Age : {} Years".format(output+1.5))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
