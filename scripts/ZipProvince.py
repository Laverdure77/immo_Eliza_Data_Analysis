import numpy as np
import pandas as pd
import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
import geopandas as gpd
import json
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Add a property to each featue in the geojson file, named 'mean_price_sqm', according to the zipcode
with open('./datas/georef-belgium-postal-codes.geojson') as f:
    data = json.load(f)

zip_prov = dict()
# Iterate over the features
for feature in data['features']:
    # Add the new column to the properties
    _zip = feature['properties']['postcode']
    _province_code = feature['properties']['prov_code']
    _province_name = feature['properties']['prov_name_fr']
    zip_prov[_zip] = {"province_code":_province_code, "province_name":_province_name }


print(zip_prov.values())
# print(zip_prov.keys())

