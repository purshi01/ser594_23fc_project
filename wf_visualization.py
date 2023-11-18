import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize():
    df = pd.read_csv("data_processed/out.csv", header=0)
    compute_summary(df)
    # Selected quantitative features
    quantitative_features = ['YrSold', 'MoSold', 'mortgage_interest', 'inflation_rates', 'OverallQual', 'OverallCond', 'GrLivArea', 'TotalBsmtSF', 'GarageCars', 'GarageArea', 'YearBuilt', 'YearRemodAdd', 'SalePrice', 'LotArea']
    
    # Qualitative features are all other columns not in the quantitative_features list
    qualitative_features = ['Neighborhood', 'Street', 'PoolQC', 'Heating', 'CentralAir']

    
    # Create scatter plots for pairs of quantitative features
    for i in range(len(quantitative_features)):
        for j in range(i+1, len(quantitative_features)):
            feature1 = quantitative_features[i]
            feature2 = quantitative_features[j]
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[feature1], y=df[feature2], ax=ax)
            ax.set_xlabel(feature1)
            ax.set_ylabel(feature2)
            ax.set_title(f"Scatter Plot: {feature1} vs {feature2}")
            fig.savefig(f"visuals/{feature1}_vs_{feature2}.png")
            plt.close(fig) 

    # Create histograms for each qualitative feature
    for feature in qualitative_features:
        fig, ax = plt.subplots(figsize=(12, 6))
        plt.xticks(rotation=45) 
        ax.tick_params(axis='x', labelsize=8) 
        sns.histplot(df[feature], ax=ax)
        ax.set_xlabel(feature)
        ax.set_ylabel("Count")
        ax.set_title(f"Histogram of {feature}")
        fig.savefig(f"visuals/{feature}_Histogram.png")
        plt.close(fig) 

    # Create a correlation matrix for selected numeric features + SalePrice
    numeric_df = df[quantitative_features].select_dtypes(include=["int64", "float64"])
    corr_matrix = numeric_df.corr()

    # Create a heatmap of the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix of Quantitative Features")
    fig.savefig("visuals/Correlation_Matrix.png")
    with open('data_processed/correlations.txt', 'w') as f:
        f.write(corr_matrix.to_string())

def compute_summary(df):
    # Selected quantitative features
    quantitative_features = ['YrSold', 'MoSold', 'mortgage_interest', 'inflation_rates', 'OverallQual', 'OverallCond', 'GrLivArea', 'TotalBsmtSF', 'GarageCars', 'GarageArea', 'YearBuilt', 'YearRemodAdd', 'SalePrice', 'LotArea']
    
    # Qualitative features are all other columns not in the quantitative_features list
    qualitative_features = ['Neighborhood', 'Street', 'PoolQC', 'Heating', 'CentralAir']
    
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