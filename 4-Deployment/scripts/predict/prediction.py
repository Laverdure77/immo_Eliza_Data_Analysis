from scripts.preprocessing.loadmodel import loadmodel

# Load model and predict using X_request
def prediction(_X_request):
    model  = loadmodel()
    return int(model.predict(_X_request.to_numpy()))