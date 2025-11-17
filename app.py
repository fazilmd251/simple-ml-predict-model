import numpy as np
from flask import Flask, render_template, request, redirect, url_for
import math
import pickle

app = Flask(__name__)

model2 = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    # Get prediction result from query parameter if present
    prediction_result = request.args.get('prediction_result')
    return render_template('index.html', prediction_result=prediction_result)

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(i) for i in request.form.values()]
    final_features = np.array(int_features).reshape(1, -1)

    prediction = model2.predict(final_features)
    output = round(prediction[0], 2)
    result = "Number of weekly rides {}".format(math.floor(output))

    # Redirect to home route with prediction result as a query parameter
    return redirect(url_for('home', prediction_result=result))

if __name__ == '__main__':
    app.run(debug=True)
