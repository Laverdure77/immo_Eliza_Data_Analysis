import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
from sklearn.metrics import classification_report


# Load the datas 
file = './datas/Immoweb_data_ok_maite.csv'
data = pd.read_csv(file)
print(data.index) 
# print(data.head(5))
# print(data.dtypes)
# print(data.index)
# Data Cleaning
# data.replace(np.NaN,'None', inplace=True)
# data.replace('None', pd.NA, inplace=True)

# Remove unnecessary datas
# Remove Duplicates (same immoweb id)
data = data.drop_duplicates('Id')                        
# Remove rows where Price is missing
data = data.drop(data[data['Price'].isna()].index)
# Remove rows where Living area is missing
data = data.drop((data[data['Living area'].isna()].index))
# Remove Apartment Group and House Group
data = data.drop(data[data['House or appartment?'] == 'APARTMENT_GROUP'].index)
data = data.drop(data[data['House or appartment?'] == 'HOUSE_GROUP'].index)
# Remove Public sales
data = data.drop(data[data['Type of sale'] == 'PUBLIC_SALE'].index)


# print(data.dtypes)
# print(data.corr())
# print(data.shape[0])

# Add Zipcode information
zip_code_data = pd.read_csv("./datas/Postal_codes.csv", sep=";")
zip_code_data['Localite'] = zip_code_data['Localite'].apply(str.lower)
data['Locality'] = data['Locality'].apply(str.lower)

# Create zip code dictionary to map the dataframe
zip_code_dict = zip_code_data.set_index('Localite')['Code'].to_dict()
data['zip_code'] = data['Locality'].map(zip_code_dict)

# Remove rows where zipcode is missing
data = data.drop(data[data['zip_code'].isna()].index)

# print(data.shape[0])
# Add Province information

data.loc[data['zip_code'].between(1000, 1299,'both'), 'Province'] = 'Bruxelles'
data.loc[data['zip_code'].between(1300, 1499,'both'), 'Province'] = 'Brabant_wallon'
data.loc[data['zip_code'].between(2000, 2999,'both'), 'Province'] = 'Anvers'
data.loc[data['zip_code'].between(3500, 3999,'both'), 'Province'] = 'Limbourg'
data.loc[data['zip_code'].between(4000, 4999,'both'), 'Province'] = 'Liege'
data.loc[data['zip_code'].between(5000, 5680,'both'), 'Province'] = 'Namur'
data.loc[data['zip_code'].between(6600, 6999,'both'), 'Province'] = 'Luxembourg'
data.loc[data['zip_code'].between(8000, 8999,'both'), 'Province'] = 'Flandre_occidentale'
data.loc[data['zip_code'].between(9000, 9999,'both'), 'Province'] = 'Flandre_orientale'
data.loc[data['zip_code'].between(1500, 1999,'both'), 'Province'] = 'Brabant_flamand'
data.loc[data['zip_code'].between(3000, 3499,'both'), 'Province'] = 'Brabant_flamand'
data.loc[data['zip_code'].between(6000, 6599,'both'), 'Province'] = 'Hainaut'
data.loc[data['zip_code'].between(7000, 7999,'both'), 'Province'] = 'Hainaut'
# print(data.head())
data = data.reset_index()
# print(data.loc(data[data['Province'].isnull()].index))
# print(data['Province'].isna().sum())
# print(data.head())

# na_rows = data.iloc[data[data['Province'].isnull()].index]
# print(na_rows)
# data.index.head()

print(data.shape[0])

data_model_house = data[data['House or appartment?'] == 'HOUSE']
data_model_house = data_model_house[['Price', 'Province', 'Living area','Number of rooms']]
data_model_house = pd.get_dummies(data_model_house, columns =['Province'],drop_first=True )
# print(data_model_house.head())
# print(data_model_house.isnull().sum())
# print(data_model_house.shape[0])

print(data_model_house.columns)
# Prepare for modeling

y = data_model_house[['Price']].to_numpy()
X = data_model_house.drop(columns='Price').to_numpy()
print(X.shape)
print(y.shape)

# Split the datas

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=46)
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