import pickle
import pandas as pd

def loadmodel():
    try:
        #Load trained model
        _model = pickle.load(open("model/model.pkl","rb"))
        print(type(_model))
        return (_model)
    except:
        print('Unable to load model!')
        return

def loadXtemplate():
    try:  
        # Load X_template df
        _X_template = pd.read_pickle("model/X_model.pkl")
        return (_X_template)
    except:
        print('Unable to load X_template!')
        return