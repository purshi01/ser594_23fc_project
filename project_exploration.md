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
DATE: Date for the house interest rate in each year
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
1995-01-01,3.06809

From mortgage_intrestrates.csv:
1971-04-02,7.33

**Interpretation:**

I have interpreted only important features which are required for this project.

YrSold: The property was sold in 2008.
MoSold: The sale occurred in February (the 2nd month).
mortgage_interest: The mortgage interest rate in the year of 1971 was 7.33%.
inflation_rate: The inflation rate in the year of 1995 was 3.06809%.
OverallQual: The overall material and finish quality of the house is rated 7 on a scale of 1-10.
OverallCond: The overall condition of the house is rated 5 on a scale of 1-10.
GrLivArea: The above-ground living area is 1710 square feet.
TotalBsmtSF: The total basement area is 856 square feet.
GarageCars: The garage can hold 2 cars.
GarageArea: The size of the garage is 548 square feet.
Neighborhood: The property is located in the 'CollgCr' neighborhood.
YearBuilt: The house was built in 2003.
YearRemodAdd: The house was last remodeled or additions made in 2003.
SalePrice: The property was sold for $208,500.
Street: The property has paved street access ('Pave').
PoolArea: The pool area is 0 square feet, indicating no pool.
PoolQC: Pool quality data is not available (NaN).
LotArea: The lot size is 8450 square feet.
Heating: The house is equipped with gas heating ('GasA').
CentralAir: The property has central air conditioning ('Y').

### Record 2

**Raw Data:**
From data_original.csv :
2,20,RL,80,9600,Pave,NA,Reg,Lvl,AllPub,FR2,Gtl,Veenker,Feedr,Norm,1Fam,1Story,6,8,1976,1976,Gable,CompShg,MetalSd,MetalSd,None,0,TA,TA,CBlock,Gd,TA,Gd,ALQ,978,Unf,0,284,1262,GasA,Ex,Y,SBrkr,1262,0,0,1262,0,1,2,0,3,1,TA,6,Typ,1,TA,Attchd,1976,RFn,2,460,TA,TA,Y,298,0,0,0,0,0,NA,NA,NA,0,5,2007,WD,Normal,181500

From inflation_rates.csv:
1995-02-01,2.6616

From mortgage_intrestrates.csv:
1971-04-09,6.3373

**Interpretation:**
I have interpreted only important features which are required for this project.

YrSold: The property was sold in 2007.
MoSold: The sale occurred in May.
mortgage_interest: The mortgage interest rate in the year of 1971 was 6.3373%.
inflation_rate: The inflation rate in the year of 1995 was 2.6616%.
OverallQual: The overall material and finish quality of the house is rated as 6 on a scale of 1-10.
OverallCond: The overall condition of the house is rated as 8 on a scale of 1-10.
GrLivArea: The above-ground living area is 1,262 square feet.
TotalBsmtSF: The total basement area is 1,262 square feet.
GarageCars: The garage can hold 2 cars.
GarageArea: The size of the garage is 460 square feet.
Neighborhood: The property is located in the 'Veenker' neighborhood.
YearBuilt: The house was built in 1976.
YearRemodAdd: The house was last remodeled or had additions made in 1976.
SalePrice: The property was sold for $181,500.
Street: The property has paved street access ('Pave').
PoolArea: The pool area is 0 square feet, indicating no pool.
PoolQC: Pool quality data is not available (NaN).
LotArea: The lot size is 9,600 square feet.
Heating: The house is equipped with gas heating ('GasA').
CentralAir: The property has central air conditioning ('Y').

## Data Sources

mortgage_interest.csv = https://fred.stlouisfed.org/series/MORTGAGE30US
data_original.csv = https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
inflation_rates.csv = https://fred.stlouisfed.org/series/UIGFULL

## Background Domain Knowledge

The real estate sector, specifically the housing market, plays a pivotal role in shaping a nation's economic trajectory. It holds sway over critical economic indicators like growth rate, employment generation, and patterns in consumer spending. For most people, buying a house is among the most significant financial decisions they will ever make. This decision is influenced by a myriad of factors, some broad in scope like macroeconomic variables, and others more specific to the individual property.

Macroeconomic indicators like interest rates and inflation rate can influence the housing market in profound ways. According to a study by Poterba (1984), interest rates, in particular, have a strong negative correlation with housing prices. When interest rates are high, mortgage costs rise, making houses less affordable and thus leading to a drop in demand and prices. Additionally, inflation can erode purchasing power, making real estate a more attractive investment as a hedge against inflation, which could drive up demand and prices[^1^].

On the micro level, the characteristics of the property itself, such as its size, age, condition, location, and other attributes, significantly impact its market value. As reported by Clapp, Rodrigues, and Ross (1997), a house's age can affect its price due to factors like wear and tear, design outdatedness, and the evolving preferences of homebuyers. Location, often touted as the most crucial factor in real estate, can determine accessibility to essential services, quality of schools, and overall desirability, all of which impact price. As the inflation rate is less and mortgage rate less house price is expensive.

Thus, making an informed decision on when to buy a house demands a thorough understanding of both these macroeconomic indicators and property-specific attributes. By studying historical housing sales data, potential buyers and investors can discern patterns, trends, and preferences that can guide their decisions, ensuring that they get the best value for their money and make a sound investment.

### References

[^1^]: Goodman, A. C., & Thibodeau, T. G. (2008). _Where are the speculative bubbles in US housing markets?_ Journal of Housing Economics, 17(2), 117-137.

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

### Visual 1 : Distribution of Neighborhoods

**Analysis:**  
This chart displays a histogram of the Neighborhood column from the dataset. It illustrates the frequency distribution of houses across different neighborhoods. This analysis is crucial for identifying which areas are more densely populated with listed properties, offering insights into the popularity or residential density of various neighborhoods. Such information could be invaluable to homebuyers, investors, or real estate professionals in understanding regional market trends and identifying areas of high or low housing density.

### Visual 2 : Relationship Between Overall Condition and Year Built

**Analysis:**  
The scatter plot provides insight into how the age of a house (`YearBuilt`) relates to its overall condition. Observing any trends here might reveal if older houses tend to be in better or worse condition compared to newer ones. This could be crucial for potential homeowners deciding between buying older, potentially historic homes versus newer constructions.

### Visual 3 : Impact of Inflation on House Prices

**Analysis:**  
This line graph depicts the relationship between house prices (SalePrice) and historical inflation rates (inflation_rates). It aims to show how inflation has possibly influenced the housing market over time. This analysis can be particularly enlightening for economists, real estate investors, and homebuyers in understanding how external economic factors like inflation impact property values, potentially guiding more informed investment or purchasing decisions.

### Visual 4 : Correlation Between Mortgage Rates and Sale Prices

**Analysis:**  
This scatter plot explores the relationship between mortgage rates (mortgage_rates) and house sale prices (SalePrice). It aims to reveal any patterns or correlations between the cost of borrowing (as indicated by mortgage rates) and the prices at which houses are sold. This visual can be particularly valuable for understanding how changes in the financial sector influence the real estate market. It offers insights for homebuyers, investors, and market analysts about the potential impact of fluctuating mortgage rates on housing affordability and investment attractiveness.

### Visual 5 : Distribution of Heating Quality

**Analysis:**  
This visualization showcases a histogram of the HeatingQC column from the dataset, which reflects the quality of heating systems in various houses. It highlights the distribution and frequency of different heating quality ratings, ranging from poor to excellent. This analysis is critical for understanding the prevalence of high-quality heating systems in the housing market. It can guide homebuyers, renovators, and real estate professionals in assessing the standard of living comfort and potential investment needed in heating system upgrades or maintenance.
