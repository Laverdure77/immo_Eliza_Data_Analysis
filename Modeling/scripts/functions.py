import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create and prepare dataset from data scrapping csv
def get_dataset(_csv_path: str) -> pd.DataFrame :
    _data = pd.read_csv(_csv_path)
    # Remove unnecessary datas
    # Remove Duplicates (same immoweb id)
    _data = _data.drop_duplicates('Id')                        
    # Remove rows where Price is missing
    _data = _data.drop(_data[_data['Price'].isna()].index)
    # Remove rows where Living area is missing
    _data = _data.drop((_data[_data['Living area'].isna()].index))
    # Remove Apartment Group and House Group
    _data = _data.drop(_data[_data['House or appartment?'] == 'APARTMENT_GROUP'].index)
    _data = _data.drop(_data[_data['House or appartment?'] == 'HOUSE_GROUP'].index)
    # Remove Public sales
    _data = _data.drop(_data[_data['Type of sale'] == 'PUBLIC_SALE'].index)
    _data['Number of rooms'] = _data['Number of rooms'].astype(int)
    _data['Number of facades'] = _data['Number of facades'].astype(int)
    # Reset index after drop
    # _data = _data.reset_index()
    return _data

# Add zipcode columns from csv, based on locality column
def add_zipcode(_zipcode_path: str,_data: pd.DataFrame, _sep=";") -> pd.DataFrame :
    # Read the zipcode csv
    zip_code_data = pd.read_csv(_zipcode_path, sep=_sep)
    # Apply str.lower to localities for better matching btw zipcode and df
    zip_code_data['Localite'] = zip_code_data['Localite'].apply(str.lower)
    _data['Locality'] = _data['Locality'].apply(str.lower)
    # Create zip code, locality dictionary
    zip_code_dict = zip_code_data.set_index('Localite')['Code'].to_dict()
    # Map the dataframe to add the zipcode column
    _data['zip_code'] = _data['Locality'].map(zip_code_dict)
    # Remove rows where zipcode is missing
    _data = _data.drop(_data[_data['zip_code'].isna()].index)
    # Reset index after drop
    # _data = _data.reset_index()
    return _data

# Add Province column based on zipcode column
def add_province(_data: pd.DataFrame) -> pd.DataFrame :
    _data.loc[_data['zip_code'].between(1000, 1299,'both'), 'Province'] = 'Bruxelles'
    _data.loc[_data['zip_code'].between(1300, 1499,'both'), 'Province'] = 'Brabant_wallon'
    _data.loc[_data['zip_code'].between(2000, 2999,'both'), 'Province'] = 'Anvers'
    _data.loc[_data['zip_code'].between(3500, 3999,'both'), 'Province'] = 'Limbourg'
    _data.loc[_data['zip_code'].between(4000, 4999,'both'), 'Province'] = 'Liege'
    _data.loc[_data['zip_code'].between(5000, 5680,'both'), 'Province'] = 'Namur'
    _data.loc[_data['zip_code'].between(6600, 6999,'both'), 'Province'] = 'Luxembourg'
    _data.loc[_data['zip_code'].between(8000, 8999,'both'), 'Province'] = 'Flandre_occidentale'
    _data.loc[_data['zip_code'].between(9000, 9999,'both'), 'Province'] = 'Flandre_orientale'
    _data.loc[_data['zip_code'].between(1500, 1999,'both'), 'Province'] = 'Brabant_flamand'
    _data.loc[_data['zip_code'].between(3000, 3499,'both'), 'Province'] = 'Brabant_flamand'
    _data.loc[_data['zip_code'].between(6000, 6599,'both'), 'Province'] = 'Hainaut'
    _data.loc[_data['zip_code'].between(7000, 7999,'both'), 'Province'] = 'Hainaut' 
    # Remove rows where Province is missing
    _data = _data.drop((_data[_data['Province'].isna()].index))
    # Reset index after drop
    # _data = _data.reset_index()
    return _data

# Add Region column based on zipcode column
def add_region(_data: pd.DataFrame) -> pd.DataFrame :
    _data.loc[_data['zip_code'].between(1000, 1299,'both'), 'Region'] = 'Brux'
    _data.loc[_data['zip_code'].between(1300, 1499,'both'), 'Region'] = 'Wallonie'
    _data.loc[_data['zip_code'].between(2000, 2999,'both'), 'Region'] = 'Flandre'
    _data.loc[_data['zip_code'].between(3500, 3999,'both'), 'Region'] = 'Flandre'
    _data.loc[_data['zip_code'].between(4000, 4999,'both'), 'Region'] = 'Wallonie'
    _data.loc[_data['zip_code'].between(5000, 5680,'both'), 'Region'] = 'Wallonie'
    _data.loc[_data['zip_code'].between(6600, 6999,'both'), 'Region'] = 'Wallonie'
    _data.loc[_data['zip_code'].between(8000, 8999,'both'), 'Region'] = 'Flandre'
    _data.loc[_data['zip_code'].between(9000, 9999,'both'), 'Region'] = 'Flandre'
    _data.loc[_data['zip_code'].between(1500, 1999,'both'), 'Region'] = 'Flandre'
    _data.loc[_data['zip_code'].between(3000, 3499,'both'), 'Region'] = 'Flandre'
    _data.loc[_data['zip_code'].between(6000, 6599,'both'), 'Region'] = 'Wallonie'
    _data.loc[_data['zip_code'].between(7000, 7999,'both'), 'Region'] = 'Wallonie'
    # Remove rows where PRegion is missing
    _data = _data.drop((_data[_data['Region'].isna()].index))
    # Reset index after drop
    # _data = _data.reset_index()
    return _data

# Slice df to target and features
def set_feat_target(_data: pd.DataFrame) -> np.ndarray:
    # Set target and features
    _y = _data[['Price']].to_numpy()
    _X = _data.drop(columns='Price').to_numpy()
    return _X, _y

# Plot regression line from intercept and coef
def regline(_slope: float, _intercept: float, _color: str ):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = _intercept + _slope * x_vals
    plt.plot(x_vals, y_vals, '--', color=_color)