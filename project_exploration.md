#### SER594: Exploratory Data Munging and Visualization

#### Predicting the Best Time to Buy a House based on Historic Housing Data(title)

#### Purushothama Shanthappa (author)

#### 18 Oct 2023 (date)

## Basic Questions

**Dataset Author(s):** Anna Montoya, DataCanary,Federal Reserve Bank of New York.

**Dataset Construction Date:**
mortgage_interest.csv = 2023
data_original.csv = 2016
inflation_rates.csv = 2023

**Dataset Record Count:**
data_original.csv = 1461
inflation_rates.csv = 346
mortgage_intrestrates.csv = 2743

**Dataset Field Meanings:**
data_original.csv
SalePrice - the property's sale price in dollars. This is the target variable that you're trying to predict.
MSSubClass: The building class
MSZoning: The general zoning classification
LotFrontage: Linear feet of street connected to property
LotArea: Lot size in square feet
Street: Type of road access
Alley: Type of alley access
LotShape: General shape of property
LandContour: Flatness of the property
Utilities: Type of utilities available
LotConfig: Lot configuration
LandSlope: Slope of property
Neighborhood: Physical locations within Ames city limits
Condition1: Proximity to main road or railroad
Condition2: Proximity to main road or railroad (if a second is present)
BldgType: Type of dwelling
HouseStyle: Style of dwelling
OverallQual: Overall material and finish quality
OverallCond: Overall condition rating
YearBuilt: Original construction date
YearRemodAdd: Remodel date
RoofStyle: Type of roof
RoofMatl: Roof material
Exterior1st: Exterior covering on house
Exterior2nd: Exterior covering on house (if more than one material)
MasVnrType: Masonry veneer type
MasVnrArea: Masonry veneer area in square feet
ExterQual: Exterior material quality
ExterCond: Present condition of the material on the exterior
Foundation: Type of foundation
BsmtQual: Height of the basement
BsmtCond: General condition of the basement
BsmtExposure: Walkout or garden level basement walls
BsmtFinType1: Quality of basement finished area
BsmtFinSF1: Type 1 finished square feet
BsmtFinType2: Quality of second finished area (if present)
BsmtFinSF2: Type 2 finished square feet
BsmtUnfSF: Unfinished square feet of basement area
TotalBsmtSF: Total square feet of basement area
Heating: Type of heating
HeatingQC: Heating quality and condition
CentralAir: Central air conditioning
Electrical: Electrical system
1stFlrSF: First Floor square feet
2ndFlrSF: Second floor square feet
LowQualFinSF: Low quality finished square feet (all floors)
GrLivArea: Above grade (ground) living area square feet
BsmtFullBath: Basement full bathrooms
BsmtHalfBath: Basement half bathrooms
FullBath: Full bathrooms above grade
HalfBath: Half baths above grade
Bedroom: Number of bedrooms above basement level
Kitchen: Number of kitchens
KitchenQual: Kitchen quality
TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)
Functional: Home functionality rating
Fireplaces: Number of fireplaces
FireplaceQu: Fireplace quality
GarageType: Garage location
GarageYrBlt: Year garage was built
GarageFinish: Interior finish of the garage
GarageCars: Size of garage in car capacity
GarageArea: Size of garage in square feet
GarageQual: Garage quality
GarageCond: Garage condition
PavedDrive: Paved driveway
WoodDeckSF: Wood deck area in square feet
OpenPorchSF: Open porch area in square feet
EnclosedPorch: Enclosed porch area in square feet
3SsnPorch: Three season porch area in square feet
ScreenPorch: Screen porch area in square feet
PoolArea: Pool area in square feet
PoolQC: Pool quality
Fence: Fence quality
MiscFeature: Miscellaneous feature not covered in other categories
MiscVal: $Value of miscellaneous feature
MoSold: Month Sold
YrSold: Year Sold
SaleType: Type of sale
SaleCondition: Condition of sale

inflation_rates.csv
DATE: Date for the inflation rate in each year
UIGFULL: Inflation rate

mortgage_interest.csv
DATE: Date for the inflation rate in each year
MORTGAGE30US: mortgage_interest

**Dataset File Hash(es):**

- Downloaded dataset:
  data_original.csv = 80ccab65fb115cbad143dbbd2bcd5577
  data_description.txt = 257555ae04270bc5c3e3a20189c2d1b7
  inflation_rates.csv = 2f7efbb3f0b2ec09e5f6645b8ef34fb5
  mortgage_intrestrates.csv = f303d5ab837c764fa3780446d1388494

- Abridged dataset:
  out.csv = 8c6e577d33bac8215e002681a96b6b18

## Interpretable Records

### Record 1

**Raw Data:**
From data_original.csv :
1,60,RL,65,8450,Pave,NA,Reg,Lvl,AllPub,Inside,Gtl,CollgCr,Norm,Norm,1Fam,2Story,7,5,2003,2003,Gable,CompShg,VinylSd,VinylSd,BrkFace,196,Gd,TA,PConc,Gd,TA,No,GLQ,706,Unf,0,150,856,GasA,Ex,Y,SBrkr,856,854,0,1710,1,0,2,1,3,1,Gd,8,Typ,0,NA,Attchd,2003,RFn,2,548,TA,TA,Y,0,61,0,0,0,0,NA,NA,NA,0,2,2008,WD,Normal,208500

From inflation_rates.csv:
1995-01-01,2.8263

From mortgage_intrestrates.csv:
1971-04-02,6.0272

**Interpretation:**

Certainly! Based on the provided data, the house in question has several characteristics that are important in determining its price. The property exhibits a moderate level of quality and is well-maintained, with an 'OverallQual' rating of 6 and an 'OverallCond' rating of 8. These ratings indicate that the house is in decent shape and features good-quality materials.

However, it's worth noting that the house was built in 1976 and has not been remodeled since. This means it might lack some modern features or updates, which could have a negative impact on its price.

On the positive side, the property boasts a relatively spacious lot ('LotArea') at 9,600 square feet and has a 2-car attached garage ('GarageCars') with an area of 460 square feet. Larger lots and garages tend to result in higher property values.

The number of bedrooms ('BedroomAbvGr') and bathrooms ('FullBath') is moderate, which should have a neutral effect on the house price.

The neighborhood ('Neighborhood') is 'Veenker,' and the specific desirability of this neighborhood can significantly affect the property's value.

In terms of the roof, the house features a gable roof ('RoofStyle') with standard composite shingles ('RoofMatl'), which is a common and cost-effective choice.

The exterior covering is 'MetalSiding,' and the quality and condition are rated as 'TA,' indicating typical quality.

as the inflation rate is less and mortgage interest rate more house price is expensive.

These factors combined paint a picture of a property that is decently sized, well-kept, and located in a neighborhood that may have varying influences on house prices. The lack of recent remodeling and the age of the house might slightly affect its price, but factors like the lot size and the garage can positively impact its value. Ultimately, the specific housing market and buyer preferences will play a role in determining the house's final price.

### Record 2

**Raw Data:**
From data_original.csv :
2,20,RL,80,9600,Pave,NA,Reg,Lvl,AllPub,FR2,Gtl,Veenker,Feedr,Norm,1Fam,1Story,6,8,1976,1976,Gable,CompShg,MetalSd,MetalSd,None,0,TA,TA,CBlock,Gd,TA,Gd,ALQ,978,Unf,0,284,1262,GasA,Ex,Y,SBrkr,1262,0,0,1262,0,1,2,0,3,1,TA,6,Typ,1,TA,Attchd,1976,RFn,2,460,TA,TA,Y,298,0,0,0,0,0,NA,NA,NA,0,5,2007,WD,Normal,181500

From inflation_rates.csv:
1995-02-01,2.6616

Frommortgage_intrestrates.csv:
1971-04-09,6.3373

**Interpretation:** It is a one-story, single-family home located in the 'Veenker' neighborhood, which can have a notable impact on property values. The overall quality of the house is rated at 6 ('OverallQual'), and the overall condition is 8 ('OverallCond'), which means it's in decent condition with good-quality materials.

However, the house was constructed in 1976 and hasn't been remodeled since. This older age may result in a lack of modern updates or features, potentially affecting the property's price negatively.

The property has a relatively spacious lot ('LotArea') of 9,600 square feet, which is often a positive factor in property valuation. It features an attached 2-car garage ('GarageCars') with an area of 460 square feet, another positive aspect as larger garages often lead to higher property values.

The number of bedrooms ('BedroomAbvGr') is three, and the number of full bathrooms ('FullBath') is two. These features are relatively typical and may not significantly influence the house price.

The roof has a gable design ('RoofStyle') with standard composite shingles ('RoofMatl'), which is a common and cost-effective choice.

The exterior covering is 'MetalSiding,' and its quality and condition are rated as 'TA,' indicating typical quality.
as the inflation rate is less and mortgage interest rate more house price will be affordable.

In summary, this house appears to be of average quality and condition, with a well-maintained exterior and a desirable neighborhood. However, its age and the lack of recent remodeling may slightly impact its price. Other factors, such as the lot size and the garage, are likely to have a more positive effect on its value. The final price will ultimately depend on the specific housing market and buyer preferences.

## Data Sources

mortgage_interest.csv = https://fred.stlouisfed.org/series/MORTGAGE30US
data_original.csv = https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
inflation_rates.csv = https://fred.stlouisfed.org/series/UIGFULL

## Background Domain Knowledge

The real estate sector, specifically the housing market, plays a pivotal role in shaping a nation's economic trajectory. It holds sway over critical economic indicators like growth rate, employment generation, and patterns in consumer spending. For most people, buying a house is among the most significant financial decisions they will ever make. This decision is influenced by a myriad of factors, some broad in scope like macroeconomic variables, and others more specific to the individual property.

Macroeconomic indicators like interest rates and inflation rate can influence the housing market in profound ways. According to a study by Poterba (1984), interest rates, in particular, have a strong negative correlation with housing prices. When interest rates are high, mortgage costs rise, making houses less affordable and thus leading to a drop in demand and prices[^1^]. Additionally, inflation can erode purchasing power, making real estate a more attractive investment as a hedge against inflation, which could drive up demand and prices[^2^].

On the micro level, the characteristics of the property itself, such as its size, age, condition, location, and other attributes, significantly impact its market value. As reported by Clapp, Rodrigues, and Ross (1997), a house's age can affect its price due to factors like wear and tear, design outdatedness, and the evolving preferences of homebuyers[^3^]. Location, often touted as the most crucial factor in real estate, can determine accessibility to essential services, quality of schools, and overall desirability, all of which impact price. As the inflation rate is less and mortgage rate less house price is expensive.

Thus, making an informed decision on when to buy a house demands a thorough understanding of both these macroeconomic indicators and property-specific attributes. By studying historical housing sales data, potential buyers and investors can discern patterns, trends, and preferences that can guide their decisions, ensuring that they get the best value for their money and make a sound investment.

### References

[^1^]: Poterba, J. M. (1984). _Tax subsidies to owner-occupied housing: an asset-market approach_. Quarterly Journal of Economics, 99(4), 729-752.
[^2^]: Goodman, A. C., & Thibodeau, T. G. (2008). _Where are the speculative bubbles in US housing markets?_ Journal of Housing Economics, 17(2), 117-137.
[^3^]: Clapp, J. M., Rodrigues, M., & Ross, S. L. (1997). _The impact of building age on residential price_. Journal of Urban Economics, 42(3), 310-334.

## Data Transformation

### Transformation 1

**Description:** Handling Missing Data  
Many datasets, especially those concerning real estate, have missing values due to various reasons like unavailability during data collection or irrelevance for certain property types. For this dataset, we replace missing numerical values with the mean and categorical values with the mode of their respective columns.

**Soundness Justification:**  
Using mean for numerical and mode for categorical variables ensures that we don't introduce bias in the data, keeping the data distribution relatively stable.

### Transformation 2

**Description:** One-Hot Encoding of Categorical Variables  
To make the dataset suitable for machine learning algorithms, we need to convert categorical variables into a format that can be provided to these algorithms. One-hot encoding is a popular method for this, where each category for each feature becomes a new column.

**Soundness Justification:**  
One-hot encoding is a standard procedure for converting categorical data into a machine-readable format without introducing ordinal relationships where they don't exist.

### Transformation 3

**Description:** Feature Scaling  
To ensure that no particular feature dominates the others due to scale, we employ feature scaling, particularly Min-Max scaling, to normalize the feature values between 0 and 1.

**Soundness Justification:**  
Feature scaling is essential, especially for distance-based algorithms, to ensure each feature has equal weightage in the algorithms.

### Transformation 4

**Description:** Feature Engineering  
Based on domain knowledge and data exploration, new features that might be more informative than some of the original features are derived. For instance, combining the basement's unfinished and finished square feet to get a total basement area might be more useful than the individual components.

**Soundness Justification:**  
Creating new features based on existing ones can sometimes capture the underlying patterns in the data better and improve the predictive power of the model.

## Visualization

### Visual 1 : Distribution of Overall Condition

**Analysis:**  
This visualization provides a histogram of the `OverallCond` column. It gives insights into the frequency distribution of the overall condition of houses in the dataset. This can be useful for understanding how many houses are in a particular condition and might help potential buyers or real estate agents to gauge the general health of houses in the area.

### Visual 2 : Relationship Between Overall Condition and Year Built

**Analysis:**  
The scatter plot provides insight into how the age of a house (`YearBuilt`) relates to its overall condition. Observing any trends here might reveal if older houses tend to be in better or worse condition compared to newer ones. This could be crucial for potential homeowners deciding between buying older, potentially historic homes versus newer constructions.

### Visual 3 : Feature Histograms (TotalBsmtSF, GrLivArea, FullBath, HalfBath, BedroomAbvGr)

**Analysis:**  
The histograms for each of the five selected features provide insights into their distribution across the dataset. These visuals can help determine the typical size of living areas, the common number of bathrooms, or the standard size of basements in the area, among other details.

### Visual 4 : Relationship Between Selected above Features and SalePrice

**Analysis:**  
Scatter plots are created for each of the five features against the sale price of the house. This is useful for understanding how each feature might influence the sale price. For instance, homes with larger living areas might have higher sale prices, or the number of bathrooms could potentially influence a home's market value.

### Visual 5 : Correlation Matrix of Selected above Features with SalePrice

**Analysis:**  
The heatmap of the correlation matrix offers a quantitative look into how selected numeric features interrelate with each other and, most importantly, with the sale price. High positive correlations might suggest that as one feature value increases, the sale price tends to increase and vice versa for negative correlations.

### Visual 6 : Mortgage and Inflation Rates Over Time

**Analysis:**  
This line plot helps visualize the trend of mortgage and inflation rates over the years. By understanding these trends, potential homeowners can make informed decisions about when to buy a house. It can also provide insights into the broader economic conditions over time.

### Visual 7 : Relationship Between SalePrice, Mortgage Rate, and Inflation Rate

**Analysis:**  
The scatter plots display how the sale price of houses relates to mortgage and inflation rates. This is crucial for understanding if economic factors like inflation or mortgage rates impact the housing market and, if so, to what extent.
