from flask import Flask, request, redirect, url_for, render_template
import pandas as pd
# import numpy as pd
import pickle
import sklearn

# Instanciate Flask kapp 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def alive():
    return render_template('request.html')

@app.route('/form',methods = ['POST'])
def form():
    # Load model
    model = pickle.load(open('4-Deployment\model\model.pkl','rb'))      
    # Load X_model df
    X_request = pd.read_pickle('4-Deployment\model\X_model.pkl')
    
    # X_request = X_request.fillna(value = 0)

    if request.method == 'POST':
        # store values from the html form
        living_area = request.form['living area']
        land_surface = request.form['land surface']
        number_rooms = request.form['number of rooms']
        number_facades = request.form['number of facades']
        garden_area = request.form['garden area']
        province = request.form['province']
        state_building = request.form['state']
        subtype = request.form['subtype']

        
        # fill the X_model dataframe with request values
        # X_model = X_model.fillna(value = 0)
        X_request.at[1,'Living area'] = int(living_area)
        X_request.at[1,'Number of rooms'] = int(number_rooms)
        X_request.at[1,'Number of facades'] = int(number_facades)
        X_request.at[1,'Land surface'] = int(land_surface)
        X_request.at[1,'Area of garden'] = int(garden_area)
        X_request.at[1,str(province)] = 1
        X_request.at[1,str(state_building)] = 1
        X_request.at[1,str(subtype)] = 1
        # print(X_request.head())
        # Replace nan values from X_request with 0
        X_request = X_request.fillna(value = 0)
        
        price_estimate = int(model.predict(X_request.to_numpy()))
        
        return render_template('result.html', est_price=price_estimate)
        # return f"{price_estimate}"
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)