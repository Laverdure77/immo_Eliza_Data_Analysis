from flask import Flask
from flask import request
from flask import render_template

from scripts.preprocessing.fillempty import fillempty
from scripts.preprocessing.loadmodel import loadXtemplate
from scripts.preprocessing.fillXtemplate import fillXtemplate
from scripts.predict.prediction import prediction

# Instanciate Flask app 
app = Flask(__name__)

# Render input form on load of the application
@app.route('/', methods=['GET'])
def alive():
    print('Alive')
    return render_template('request.html')

# On submit, predict the price using the model
@app.route('/form',methods = ['POST'])
def form():
    
    if request.method == 'POST':
        # Load an empty dataframe with the same column names as X_test
        X_template = loadXtemplate()

        # Fill the X_template dataframe with values from the html form
        X_request = fillXtemplate(X_template)
        
        # Replace nan values from X_request with 0
        X_request_cleaned = fillempty(X_request)
        
        # Prediction
        price_estimate = prediction(X_request_cleaned)
        
        return render_template('result.html', est_price=price_estimate)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')