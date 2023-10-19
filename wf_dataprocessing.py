import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler

def process():
  """
  Preprocess the data for machine learning.
  """

  # Read the data from the CSV file.
  df = pd.read_csv("data_original/data_original.csv")
  mortgage_interest = pd.read_csv("data_original/mortgage_interest.csv")
  inflation_rates = pd.read_csv("data_original/inflation_rates.csv")
  df = pd.read_csv("data_original/data_original.csv")
  df = pd.DataFrame(df)

  # Extract the year from the "DATE" column in the mortgage_interest dataset
  mortgage_interest["Year"] = pd.to_datetime(mortgage_interest["DATE"]).dt.year

  # Group and calculate the mean for mortgage interest rates by year
  mortgage_interest = mortgage_interest.groupby("Year")["MORTGAGE30US"].mean().reset_index()

  # Round the mean values to the nearest integer
  mortgage_interest["MORTGAGE30US"] = mortgage_interest["MORTGAGE30US"].round(4)

  # Rename the columns in mortgage_interest
  mortgage_interest = mortgage_interest.rename(columns={"MORTGAGE30US": "mortgage_interest"})

  # Merge the mortgage interest data into the main DataFrame based on "YrSold" and "Year"
  df = pd.merge(df, mortgage_interest, how="left", left_on="YrSold", right_on="Year")

  # Extract the year from the "DATE" column in the inflation_rates dataset
  inflation_rates["Year"] = pd.to_datetime(inflation_rates["DATE"]).dt.year

  # Group and calculate the mean for inflation rates by year
  inflation_rates = inflation_rates.groupby("Year")["UIGFULL"].mean().reset_index()

  # Rename the columns in inflation_rates
  inflation_rates = inflation_rates.rename(columns={"UIGFULL": "inflation_rates"})

  # Round the mean values to the nearest integer
  inflation_rates["inflation_rates"] = inflation_rates["inflation_rates"].round(4)

  # Merge the inflation rates data into the main DataFrame based on "YrSold" and "Year"
  df = pd.merge(df, inflation_rates, how="left", left_on="YrSold", right_on="Year")

  # Remove duplicate rows
  df = df.drop_duplicates()

  # Drop the redundant "Year" columns
  df.drop(["Year_x", "Year_y"], axis=1, inplace=True)

  df.drop(["MiscFeature"], axis=1, inplace=True)

  # Create a boxplot of the `OverallCond` column.
  sns.boxplot(df["OverallCond"])

  # Fill in missing values in the `MasVnrType` column with the most common value.
  mode_value = df["MasVnrType"].mode().iloc[0] if not df["MasVnrType"].mode().empty else "None"
  df["MasVnrType"].fillna(mode_value, inplace=True)

  # Fill in missing values in the `MasVnrType` column with the most common value.
  mode_value = df["Alley"].mode().iloc[0] if not df["Alley"].mode().empty else "None"
  df["Alley"].fillna(mode_value, inplace=True)

  # Fill in missing values in the `MasVnrType` column with the most common value.
  mode_value = df["PoolQC"].mode().iloc[0] if not df["PoolQC"].mode().empty else "None"
  df["PoolQC"].fillna(mode_value, inplace=True)

  # Fill in missing values in the `LotFrontage` column with the mean value.
  df["LotFrontage"].fillna(df["LotFrontage"].mean(), inplace=True)

  # Fill in missing values in the `MasVnrArea` column with the mean value.
  df["MasVnrArea"].fillna(df["MasVnrArea"].mean(), inplace=True)

  # Fill in missing values in the `GarageType` column with the most common value.
  df["GarageType"].fillna("Attchd", inplace=True)

  # Fill in missing values in the `GarageYrBlt` column with the mean value.
  df["GarageYrBlt"].fillna(df["GarageYrBlt"].mean(), inplace=True)

  # Convert the `GarageFinish` column to a numerical variable.
  list_ls = list(df["GarageFinish"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Fin":
      list_ls[el] = 3
    elif list_ls[el] == "RFn":
      list_ls[el] = 2
    elif list_ls[el] == "Unf":
      list_ls[el] = 1
  df["GarageFinish"] = list_ls

  # Fill in missing values in the `GarageFinish` column with the mean value.
  df["GarageFinish"].fillna(df["GarageFinish"].mean(), inplace=True)

  # Fill in missing values in the `Fence` column with 0.
  df["Fence"].fillna(0, inplace=True)

  # Convert the `Fence` column to a binary variable.
  list_ls = list(df["Fence"])
  for el in range(len(list_ls)):
    if list_ls[el] != 0:
      list_ls[el] = 1
  df["Fence"] = list_ls

  # Convert the `Electrical` column to a binary variable.
  list_ls = list(df["Electrical"])
  for el in range(len(list_ls)):
    if list_ls[el] == "SBrkr":
      list_ls[el] = 1
    else:
      list_ls[el] = 0
  df["Electrical"] = list_ls

  # Convert the `CentralAir` column to a binary variable.
  list_ls = list(df["CentralAir"])
  for el in range(len(list_ls)):
    if list_ls[el] == "No":
      list_ls[el] = 0
    elif list_ls[el] == "Yes":
      list_ls[el] = 1
  df["CentralAir"] = list_ls

  # Convert the `PavedDrive` column to a binary variable.
  list_ls = list(df["PavedDrive"])
  for el in range(len(list_ls)):
    if list_ls[el] == "N":
      list_ls[el] = 0
    else:
      list_ls[el] = 1
  df["PavedDrive"] = list_ls

  # Convert the `BsmtFinType1` column to a numerical variable.
  list_ls = list(df["BsmtFinType1"])
  for el in range(len(list_ls)):
    if list_ls[el] == "GLQ":
      list_ls[el] = 5
    elif list_ls[el] == "ALQ":
      list_ls[el] = 4
    elif list_ls[el] == "BLQ":
      list_ls[el] = 3
    elif list_ls[el] == "Rec":
      list_ls[el] = 2
    elif list_ls[el] == "LwQ":
      list_ls[el] = 1
    elif list_ls[el] == "Unf":
      list_ls[el] = 0
  df["BsmtFinType1"] = list_ls

  # Fill in missing values in the `BsmtFinType1` column with the mean value.
  df["BsmtFinType1"].fillna(df["BsmtFinType1"].mean(), inplace=True)

  # Convert the `BsmtFinType2` column to a numerical variable.
  list_ls = list(df["BsmtFinType2"])
  for el in range(len(list_ls)):
    if list_ls[el] == "GLQ":
      list_ls[el] = 5
    elif list_ls[el] == "ALQ":
      list_ls[el] = 4
    elif list_ls[el] == "BLQ":
      list_ls[el] = 3
    elif list_ls[el] == "Rec":
      list_ls[el] = 2
    elif list_ls[el] == "LwQ":
      list_ls[el] = 1
    elif list_ls[el] == "Unf":
      list_ls[el] = 0
  df["BsmtFinType2"] = list_ls

  # Fill in missing values in the `BsmtFinType2` column with the mean value.
  df["BsmtFinType2"].fillna(df["BsmtFinType2"].mean(), inplace=True)

  # Convert the `FireplaceQu` column to a numerical variable.
  list_ls = list(df["FireplaceQu"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["FireplaceQu"] = list_ls

  # Fill in missing values in the `FireplaceQu` column with the mean value.
  df["FireplaceQu"].fillna(df["FireplaceQu"].mean(), inplace=True)

  # Convert the `GarageQual` column to a numerical variable.
  list_ls = list(df["GarageQual"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["GarageQual"] = list_ls

  # Fill in missing values in the `GarageQual` column with the mean value.
  df["GarageQual"].fillna(df["GarageQual"].mean(), inplace=True)

  # Convert the `GarageCond` column to a numerical variable.
  list_ls = list(df["GarageCond"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["GarageCond"] = list_ls

  # Fill in missing values in the `GarageCond` column with the mean value.
  df["GarageCond"].fillna(df["GarageCond"].mean(), inplace=True)

  # Convert the `KitchenQual` column to a numerical variable.
  list_ls = list(df["KitchenQual"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["KitchenQual"] = list_ls

  # Convert the `HeatingQC` column to a numerical variable.
  list_ls = list(df["HeatingQC"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["HeatingQC"] = list_ls

  # Convert the `ExterQual` column to a numerical variable.
  list_ls = list(df["ExterQual"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["ExterQual"] = list_ls

  # Convert the `ExterCond` column to a numerical variable.
  list_ls = list(df["ExterCond"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["ExterCond"] = list_ls

  # Convert the `BsmtQual` column to a numerical variable.
  list_ls = list(df["BsmtQual"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["BsmtQual"] = list_ls

  # Convert the `BsmtCond` column to a numerical variable.
  list_ls = list(df["BsmtCond"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Ex":
      list_ls[el] = 5
    elif list_ls[el] == "Gd":
      list_ls[el] = 4
    elif list_ls[el] == "TA":
      list_ls[el] = 3
    elif list_ls[el] == "Fa":
      list_ls[el] = 2
    elif list_ls[el] == "Po":
      list_ls[el] = 1
  df["BsmtCond"] = list_ls

  # Convert the `BsmtExposure` column to a numerical variable.
  list_ls = list(df["BsmtExposure"])
  for el in range(len(list_ls)):
    if list_ls[el] == "Gd":
      list_ls[el] = 3
    elif list_ls[el] == "Av":
      list_ls[el] = 2
    elif list_ls[el] == "Mn":
      list_ls[el] = 1
    elif list_ls[el] == "No":
      list_ls[el] = 0
  df["BsmtExposure"] = list_ls

  # Fill in missing values in the `BsmtExposure` column with the mean value.
  df["BsmtExposure"].fillna(df["BsmtExposure"].mean(), inplace=True)

  # Fill in missing values in the `BsmtCond` column with the mean value.
  df["BsmtCond"].fillna(df["BsmtCond"].mean(), inplace=True)

  # Fill in missing values in the `BsmtQual` column with the mean value.
  df["BsmtQual"].fillna(df["BsmtQual"].mean(), inplace=True)

  # Convert the `MSSubClass` column to a categorical variable.
  df["MSSubClass"] = df["MSSubClass"].astype("object")

  for column in df.columns:
    if df[column].dtype in ["int64", "float64"]:
      # Calculate the 25th and 75th percentiles of the column.
      q1 = np.percentile(df[column], 25)
      q3 = np.percentile(df[column], 75)

      # Calculate the interquartile range (IQR).
      iqr = q3 - q1

      # Calculate the lower and upper outlier bounds.
      lower_bound = q1 - 1.5 * iqr
      upper_bound = q3 + 1.5 * iqr

    for column in df.columns:
     if df[column].dtype in ["int64", "float64"]:
        # Calculate the 25th and 75th percentiles of the column.
        q1 = np.percentile(df[column], 25)
        q3 = np.percentile(df[column], 75)

        # Calculate the interquartile range (IQR).
        iqr = q3 - q1

        # Calculate the lower and upper outlier bounds.
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Replace any values in the column that are less than the lower bound or
        # greater than the upper bound with the median value.
        df.loc[df[column] < lower_bound, column] = np.median(df[column]).astype(df[column].dtype)
        df.loc[df[column] > upper_bound, column] = np.median(df[column]).astype(df[column].dtype)


    from sklearn.preprocessing import OneHotEncoder

    # Create a OneHotEncoder object
    ohe = OneHotEncoder()

    # Convert the categorical data in the DataFrame `df` to numerical data
    data6 = pd.get_dummies(df, dtype="int64")

    # Standardize the data using the StandardScaler class
    scaler = StandardScaler()
    scaler.fit(data6)

    # Transform the standardized data into a new DataFrame
    data7 = pd.DataFrame(scaler.transform(data6), index=data6.index, columns=data6.columns)

    # Drop the "Id" column from the new DataFrame
    data7.drop("Id", inplace=True, axis=1)

    file_name = "data_processed/out.csv"

    df.to_csv(file_name, index=False)
      
