# InsurancePremiumEstimator

## Problem Statement
The objective is to develop a machine learning-based insurance premium estimator using customer demographic and health-related data. The aim is to predict the insurance premium cost for individuals.

## Target Metric
- **R² Score**: Measures the proportion of variance explained by the model.
- **RMSE**: Root Mean Square Error to measure prediction accuracy.

## Exploratory Data Analysis (EDA)
- Univariate and Bivariate analysis were performed.
- Outliers were identified using IQR and Z-score.
- New features like BMI, BMI Category, Health Risk Flag and Surgery Severity were engineered.
- Demographic trends and health condition distributions were visualized.

## Hypothesis Testing
Performed to validate statistical significance:
- T-tests between premium and binary health factors (e.g., diabetes, chronic diseases).
- ANOVA for BMI Category and Surgery Severity.
- Chi-square tests for categorical relationships.
- Correlation tests (Pearson, Spearman) for Premium ~ BMI.

## Machine Learning Modeling
- Data preprocessing included scaling and missing value imputation.
- Models used: Linear Regression, Random Forest, XGBoost
- Hyperparameter tuning was done using `GridSearchCV` with `cross_val_score`.

### Model Performance
| Model          | Mean R² | Max R² | Mean RMSE |
|----------------|---------|--------|------------|
| Linear Reg.    | 0.6357  | —      | —          |
| Random Forest  | 0.7407  | 0.8592 | 3135.25    |
| XGBoost        | 0.7323  | 0.8392 | 3190.08    |
| Stacking Model | 0.7430  | 0.8523 | 3122.99    |

## Deployment
- **Streamlit App**: Created for real-time premium prediction using an intuitive web interface.
- **Flask API**: A backend endpoint `/predict` accepts JSON input and returns predicted premiums.
- **Pickle Files**: Trained model and scaler saved as `premium_model.pkl` and `scaler.pkl`.

## 💡 Recommendations
- Collect more real-world data, especially for rare cases like transplants.
- Incorporate additional features such as smoking habits, alcohol consumption, physical activity, and income. These are often   strong predictors of long-term health costs and can improve model accuracy and fairness.
- Use clustering or risk scores to segment customers into risk bands.
- Develop mobile or embedded solutions for insurance agents.
 
