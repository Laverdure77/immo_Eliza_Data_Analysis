import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model


# Load the datas 
file = './datas/Immoweb_data_ok_maite.csv'
data = pd.read_csv(file)
print(data.head(5))

# Data Cleaning
data.replace(np.NaN,'None', inplace=True)
data.replace('None', pd.NA, inplace=True)

# Remove unnecessary datas
# Remove Duplicates (same immoweb id)
data.drop_duplicates('Id')                        
# Remove rows where Price is missing
data = data.drop(data[data['Price'].isna()].index)
# Remove rows where Living area is missing
data.drop((data[data['Living area'].isna()].index), inplace=True)
# Remove Apartment Group and House Group
data.drop(data[data['House or appartment?'] == 'APARTMENT_GROUP'].index, inplace=True)
data.drop(data[data['House or appartment?'] == 'HOUSE_GROUP'].index, inplace=True)

# New columns
# Creat new column with price per square meter
data['price_square_meters'] = (data['Price'] / data['Living area'])
# Make sure the data type of the new column is numeric
data['price_square_meters'] = (pd.to_numeric(data['price_square_meters'], errors='coerce')).round(2)

print(data.head())
