from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

from flask_cors import CORS

from scripts.preprocessing.fillempty import fillempty
from scripts.preprocessing.loadmodel import loadXtemplate
from scripts.preprocessing.fillXtemplate import fillXtemplate
from scripts.predict.prediction import prediction

# Instanciate Flask app 
app = Flask(__name__)
# Allows cross origin to all routes
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

# Render input form on load of the application
@app.route('/', methods=['GET'])
def alive():
    print('Alive')
    return render_template('request.html', est_price=0)

# On submit, predict the price using the model
@app.route('/form',methods = ['POST'])
def form():
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if request.method == 'POST':
        # Load an empty dataframe with the same column names as X_test
        X_template = loadXtemplate()
        
        # Fill the X_template dataframe with values from the html form
        X_request = fillXtemplate(X_template)
        
        # Replace nan values from X_request with 0
        X_request_cleaned = fillempty(X_request)
        
        # Prediction
        price_estimate = f'{prediction(X_request_cleaned):,d}'
        response = jsonify(prediction = 'ok', result = price_estimate)
        print(f"prediction returned: {response}")
        
        return response

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')