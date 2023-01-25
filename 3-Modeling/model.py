import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
from sklearn.metrics import classification_report

from scripts.functions import get_dataset
from scripts.functions import add_zipcode
from scripts.functions import add_province
from scripts.functions import set_feat_target


# Load the datas 
file = './datas/Immoweb_data_ok_maite.csv'
data = get_dataset(file)
# Add zipcode column
zip_path = "./datas/Postal_codes.csv"
data = add_zipcode(zip_path, data)
# Add Province column
data = add_province(data)

# Select columns for modeling
data_model_house = data[data['House or appartment?'] == 'HOUSE'][['Price', 'Province', 'Living area','Number of rooms']]
# Get dummies for Province columns
data_model_house = pd.get_dummies(data_model_house, columns =['Province'],drop_first=True )
# Split features, target
X, y = set_feat_target(data_model_house)
# Split into train, test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 46)
# Standardisation
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Train the model
regressor = linear_model.LinearRegression()
regressor.fit(X_train, y_train)
accuracy_train = regressor.score(X_train, y_train)
print(accuracy_train)

# Test the model
accuracy_test = regressor.score(X_test, y_test)
print(accuracy_test)

# Prediction
pred_test = regressor.predict(X_test)

# print(X_test[:,1].shape[0])
# print(y_test.shape[0])
# Plot the predicted values against the input values

plt.scatter(X_train[:,0], y_train, color='blue')
# plt.plot(X_train, pred_train, color='red')
plt.scatter(X_test[:,0], y_test, color='green')
plt.scatter(X_test[:,0], pred_test, color='orange')


# Label the plot
plt.title("Price VS Features")
plt.xlabel('Features')
plt.ylabel('Price')

# Show the plot
plt.show()
plt.close()