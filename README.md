# Industrial Machine Failure Prediction

## Project Overview
This project uses machine learning to predict industrial machine failures based on operating conditions such as temperature, rotational speed, torque, and tool wear.

The project uses three machine learning models: Logistic Regression, K-Nearest Neighbors (KNN), and Random Forest. The Random Forest model is deployed as a web application using Streamlit and Render.

## Deployment
**Live Application:**  
https://machine-failure-prediction2.onrender.com

## Dataset
- **Dataset:** AI4I 2020 Predictive Maintenance Dataset
- **Total Records:** 10,000
- **Input Features:** 6
- **Target Variable:** `Machine failure`
  - `0` – No Machine Failure
  - `1` – Machine Failure

## Machine Learning Models
1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Random Forest

**Selected Model for Deployment:** Random Forest

## Model Performance

| Metric | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 82.95% | 14.55% | 82.35% | 24.72% | 90.77% |
| K-Nearest Neighbors | 93.35% | 30.54% | 75.00% | 43.40% | 89.74% |
| Random Forest | 96.90% | 53.19% | 73.53% | 61.73% | 96.83% |

Random Forest achieved the highest accuracy, precision, F1-score, and ROC-AUC among these three models. Logistic Regression achieved the highest recall.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit
- Joblib
- GitHub
- Render


## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/PAcharya204/Machine-Failure-Prediction2.git
