import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from feature import featureExtraction

filename = 'model.pkl'
# filename = 'model.pkl'

xgb = pickle.load(open(filename, 'rb'))


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def predict():
    result=None
    if request.method == 'POST':
        url = request.form['url']        
        sample = pd.DataFrame(np.array([[int(x) for x in featureExtraction(url)]]))
        print(sample)
        prediction= xgb.predict(sample)
        print(prediction)
        if  prediction==1: #[0] == 1:
            result='Phishing'
        elif  prediction ==0: #[0] == 0:
            result = 'Legit'
        return render_template('index.html', type= result)
    else: 
        return render_template('index.html', type= None)


if __name__ == '__main__':
    app.run(debug=True)
