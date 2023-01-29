# Immo_Eliza

## Data Scrapping

to be completed

## Data Analysis  

### Main jupyter note book

- Clean the dataset  
- Remove unnecessary datas  
- Adding new columns regarding the purpose of the analysis ( price per square meter)
- Remove outliers
- Plot data and regression model using SeaBorn library:

#### Price per square meters vs price

![Alt text](Graphs/PSQMvsPrice.png)  

### Mapzip jupyter notebook

- From open data Wallonie-Bruxelles website, download csv and geojson files containing zip code and geometry for Belgiuum
- Based on those files, create a dictionary storing localities and zip codes.
- Add a new column in my dataframe to map the zip code for each row.
- Group my dataframe by zip code
- Add a new column, giving me the mean price per square meter for each zip code.
- Save the result in csv format: zip_price_sqm_meters.csv

### Map_belgium jupyter notebook

- Add column in the zip code geojson file, with mean price per zipcode, from the zip_price_sqm_meters.csv created from previous notebook.  
- With the use of GEOPANDAS, display the map of belgium, showing the mean price per square meter.
- color scaling each city accordingly.
- Due to lack of naming convention on the immo website, mapping of the localities, zipcode led to loss of relevant datas
- The coverage of the map shows empty areas
- Solution found to solve this issue, but no time to implement in the given time. (Improve scrapping process according to the result to achieve, work on the data from the zip code geojson file, to improve mapping of localities, zip code, provinces...)

#### Belgium map mean price per square meters  

![Alt text](Graphs/MapBelgiumPSQM.png)

## Data Modeling

### Modeling the price of houses across Belgium

Time line for this project: 1 week.

From the datas collected, try to model the price of houses across Belgium, based on the following features:
living area, number of rooms, number of facades, state of building,  
land surface, area of garden, subtype, and province.  

Using sklearn library, I compared the result of two models : LinearRegression and GradientBoost.
The last one giving me the best score.
Using cross validation to check the consistency of the results, shows a dramatic drop of the results.
Possible reasons:
Low numbers of rows fitted in the model: from 23000 to 5000 after cleaning and selecting relevant datas.  
Even thought outliers have been managed, some strange point seems to remain in th dataset, requirering more investigation.  
keep row zip code information instaed of grouping by province could increase the performance of the models.  
Investigate on using standardisation of normalisation to improve model score.  
Avoid repalcing missing values by mean or median.

#### Data Cleaning

- load the datas from csv file.  
- adding columns for zip code, province and region.  
- Ensure the type of each column is consistent  

#### Correlation

- Explore Correlation between features  
![Alt text](Graphs/corr_matrix.png)
![Alt text](Graphs/corr_to_price.png)

#### Manage outliers

Remove outliers.  
State of the dataset before and after removing outliers on price for example:
![Alt text](Graphs/before_outliers-price.png)
![Alt text](Graphs/after_outliers-price.png)

#### Select target and features for modeling

-Target: House price  
-Features: selected according to correlation  
-Convert categorical variable into dummy/indicator variables  
-Different type of normalisation tested  

#### Linear Regression

Regressor used : LinearRegression and GradientBoostingRegressor from sklearn

Results:  
Regressor score

![Alt text](Graphs/Coef.png)  

Metrics

![Alt text](Graphs/Coef2.png)  
![Alt text](Graphs/cross_validation_values.png)  

Regression line Price vs Living area and number of rooms  

![Alt text](Graphs/price_vs_Living_area.png)
![Alt text](Graphs/price_vs_rooms.png)  

Cross validation  
![Alt text](Graphs/cross_validation.png)  

#### Interpretation

compare model : reln and rad improvedon gradboost
1 week
scoreon test not fantastic
some wierd point to investigate, time out for project
reduced nbr rows
using other model
increase dataset
hyper paramters finetuning
normalisation check only on num valuesn ot apply globally, or not for grad boos, managing internally


