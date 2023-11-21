#### SER594: Machine Learning Evaluation

#### Predicting the Best Time to Buy a House based on Historic Housing Data (title)

#### Purushothama Shanthappa (author)

#### (11/20/2023)

## Evaluation Metrics

### Metric 1

**Name:** Mean Squared Error (MSE)

**Choice Justification:** MSE is chosen as it directly measures the average of the squares of the errors or deviations. It's particularly useful in a regression context like real estate pricing, as it gives an idea of the magnitude of error made by the model.

**Interpretation:** Lower values of MSE indicate better performance. It helps in understanding the average squared difference between the estimated values and the actual value, which is crucial for accurate price predictions.

### Metric 2

**Name:** R-squared (R²)

**Choice Justification:** R-squared is a statistical measure that represents the proportion of the variance for the dependent variable that's explained by the independent variables in a regression model. It's a key metric for evaluating the fit of our model to the variance observed in the actual data.

## Alternative Models

For each alternative model, this section describes its construction relative to the initial model and its performance during evaluation. The best alternative created is also included.

### Alternative 1: Linear Regression

**Construction:** This model is a standard linear regression implemented without any form of regularization. It serves as the foundational model, using basic linear relationships between features and the target variable.

**Evaluation:** The model resulted in a Mean Squared Error (MSE) of approximately 1.282 billion and an R-squared (R²) value of 0.833. This performance establishes a baseline for comparison with more complex models. Its relatively higher MSE indicates room for improvement in accuracy.

### Alternative 2: Gradient Boosting

**Construction:** The Gradient Boosting model was constructed with parameter tuning to optimize its performance. It builds on the linear regression model by using an ensemble of decision trees to reduce errors sequentially.

**Evaluation:** The Gradient Boosting model showed a significant improvement in performance over the Linear Regression model, with an MSE of approximately 836.9 million and an R² of 0.891. This indicates a substantial increase in prediction accuracy and the model's ability to explain the variance in real estate prices.

### Alternative 3: Random Forest

**Construction:** This model is a Random Forest Regression, constructed with a specific number of estimators. It extends the concept of a single decision tree to an ensemble approach, where multiple decision trees are used to improve predictive accuracy and control over-fitting.

**Evaluation:** The Random Forest model achieved an MSE of approximately 969.5 million and an R² of 0.874. It offers competitive performance, with substantial error reduction and a high level of explanation of the variance, although slightly lower than the Gradient Boosting model.

## Best Model

**Model:** Gradient Boosting : Based on the evaluation metrics, Gradient Boosting is the best model with the lowest MSE and highest R-squared, indicating its superior performance in predicting real estate prices accurately.
