import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize():
    df = pd.read_csv("data_processed/out.csv", header=0)
    compute_summary(df)

    # Create a histogram of the `OverallCond` feature
    fig, ax = plt.subplots()
    sns.histplot(df["OverallCond"], ax=ax)
    ax.set_xlabel("Overall Condition")
    ax.set_ylabel("Number of houses")
    ax.set_title("Distribution of Overall Condition")
    fig.savefig("visuals/OverallCondition_Distribution.png")

    # Create a scatter plot of the `OverallCond` and `YearBuilt` features
    fig, ax = plt.subplots()
    sns.scatterplot(
        x=df["OverallCond"],
        y=df["YearBuilt"],
        hue=df["YearBuilt"] > 2000, # Not the best hue condition, but keeping it as it was
        ax=ax,
    )
    ax.set_xlim(1, 10)
    ax.set_xlabel("Overall Condition")
    ax.set_ylabel("Year Built")
    ax.set_title("Relationship Between Overall Condition and Year Built")
    fig.savefig("visuals/OverallCondition_vs_YearBuilt.png")

    features = ["TotalBsmtSF", "GrLivArea", "FullBath", "HalfBath", "BedroomAbvGr"]

    feature_map = {
        "TotalBsmtSF": "Total square feet of basement area",
        "GrLivArea": "Above grade (ground) living area square feet",
        "FullBath": "Full bathrooms above grade",
        "HalfBath": "Half bathrooms above grade",
        "BedroomAbvGr": "Above ground bedrooms per household"
    }

    # Create a histogram for each remaining feature
    for feature, description in feature_map.items():
        fig, ax = plt.subplots()
        sns.histplot(df[feature], ax=ax)
        ax.set_xlabel(description)
        ax.set_ylabel("Number of houses")
        ax.set_title("Distribution of " + description)
        fig.savefig("visuals/"+description+"_Distribution.png")

    # Create a scatter plot of each remaining feature vs. SalePrice
    for feature, description in feature_map.items():
        fig, ax = plt.subplots()
        sns.scatterplot(
            x=df[feature], y=df["SalePrice"], ax=ax
        )
        ax.set_xlabel(description)
        ax.set_ylabel("SalePrice")
        ax.set_title("Relationship b/w " + description + " and SalePrice")
        fig.savefig("visuals/"+description+"_vs_SalePrice.png")

    # Create a correlation matrix for selected numeric features + SalePrice
    numeric_df = df[features + ["SalePrice", "OverallCond", "YearBuilt", "mortgage_interest", "inflation_rates"]].select_dtypes(include=["int64", "float64"])
    corr_matrix = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=df['YrSold'], y=df['mortgage_interest'], label='Mortgage Rate', ax=ax)
    sns.lineplot(x=df['YrSold'], y=df['inflation_rates'], label='Inflation Rate', ax=ax)
    ax.set_title("Mortgage and Inflation Rates Over Time")
    ax.set_ylabel("Rate (%)")
    ax.set_xlabel("Year")
    plt.legend()
    fig.tight_layout()
    fig.savefig("visuals/Mortgage_Inflation_Rates.png")

    # Scatter plot to show relationship between SalePrice, Mortgage Rate, and Inflation Rate
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df['mortgage_interest'], y=df['SalePrice'], label='Mortgage Rate', ax=ax)
    sns.scatterplot(x=df['inflation_rates'], y=df['SalePrice'], label='Inflation Rate', ax=ax)
    ax.set_title("Relationship between SalePrice and Rates")
    ax.set_xlabel("Rate (%)")
    ax.set_ylabel("SalePrice")
    plt.legend()
    fig.tight_layout()
    fig.savefig("visuals/SalePrice_vs_Rates.png")

    # Create a heatmap of the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")
    fig.savefig("visuals/Correlation_Matrix.png")
    with open('data_processed/correlations.txt', 'w') as f:
        f.write(corr_matrix.to_string())

def compute_summary(df):
    # Selected quantitative features
    quantitative_features = ["OverallCond", "YearBuilt", "TotalBsmtSF", "GrLivArea", "SalePrice", "mortgage_interest", "inflation_rates"]
    
    # Qualitative features are all other columns not in the quantitative_features list
    qualitative_features = ["Neighborhood","Street","HouseStyle"]
    
    # Initializing an empty list to store the summary
    summary = []
    summary.append("*************quantitative features*************")
    summary.append("")
    # Generate summary for quantitative features
    for feature in quantitative_features:
        if feature in df.columns:
            min_value = df[feature].min()
            max_value = df[feature].max()
            median_value = df[feature].median()
            
            summary.append(f"Feature: {feature}")
            summary.append(f"Min: {min_value}")
            summary.append(f"Max: {max_value}")
            summary.append(f"Median: {median_value}")
            summary.append("") # adding an empty line for better readability
    
    summary.append("*************qualitative features*************")
    summary.append("")
    # Generate summary for qualitative features
    for feature in qualitative_features:
        if feature in df.columns:
            categories_count = df[feature].nunique()
            most_frequent = df[feature].mode().tolist()
            least_frequent_count = df[feature].value_counts().min()
            least_frequent = df[feature].value_counts()[df[feature].value_counts() == least_frequent_count].index.tolist()
            
            summary.append(f"Feature: {feature}")
            summary.append(f"Number of Categories: {categories_count}")
            summary.append(f"Most Frequent: {most_frequent}")
            summary.append(f"Least Frequent: {least_frequent}")
            summary.append("") # adding an empty line for better readability
    
    # Save to summary.txt
    with open("data_processed/summary.txt", "w") as file:
        file.write("\n".join(summary))