# Enhancing-Decision-Making-with-AI-for-Dynamic-Business-Insight-Predictions
The project utilizes a hybrid modeling approach to address key business challenges by leveraging historical data. It integrates multiple machine learning models, each tailored to a specific objective. ARIMA (AutoRegressive Integrated Moving Average) is employed for time-series forecasting, allowing accurate predictions of future sales and revenue by analyzing trends, seasonality, and past patterns. Linear Regression is used for profit prediction by modeling the relationship between revenue, cost, and other influencing business variables. To support pricing strategies, Ordinary Least Squares (OLS) regression helps optimize prices based on historical pricing performance and market response.
These models are trained and validated using historical data, and their performance is evaluated through established metrics like RMSE, R², and MAE.
The system's results are presented through a dynamic Streamlit dashboard, enabling real-time interaction with the models. Business analysts and decision-makers can input new data, explore different scenarios, and visualize the impact of changes in pricing, sales strategies, and customer segmentation.
By integrating these machine learning techniques into a user-friendly platform, the AI-driven business insight system helps organizations improve decision-making, optimize pricing strategies, and segment customers effectively. The system's adaptability also allows for future enhancements, such as incorporating deep learning models, expanding dashboard functionalities, and addressing additional business challenges, like inventory management or marketing campaign optimization. This system presents a powerful tool for organizations looking to leverage AI for smarter, data-driven decision-making.

---
## Workflow Chart
![image](https://github.com/user-attachments/assets/d5efa378-76c4-4476-b7ec-a1aad32cfd10)

---

## 🚀 KEY TASKS
- Data cleaning and transformation
- Feature engineering (e.g., encoding, scaling)
- Time-series data handling for ARIMA
- Model training and testing
- Hyperparameter optimization
- Prediction generation for sales, profit, price, and customer segmentation
- Displaying prediction results through visualizations (e.g., graphs, charts)
- Real-time interactivity for scenario analysis
- User-friendly interface for non-technical users

![image](https://github.com/user-attachments/assets/cfbc3a83-63b6-47ce-894d-048d6d6afe64)

---

## Project Novelty : 

Hybrid Modeling Approach: Integrates time-series (ARIMA) and machine learning models (linear regression, OLS, KNN) to provide a comprehensive suite of business insights.
Custom Streamlit Dashboard: Develops an interactive Streamlit app for real-time data visualization and dynamic interaction with predictive models.
Predictive Analytics Integration: Seamlessly integrates predictive analytics into existing business workflows, allowing for continuous real-time updates and actionable insights.

---

## 🛠️ Tech Stack  

- **Frontend**: StreamLit-Dashboard 
- **Backend**: Python, Machine Learning, Scikit-learn 
- **Database**: Comma Seperated Value Files 
- **Tools**: Jupiternotebook

---

## 🚀 Features

1. Sales Forecasting Using SARIMA

    SARIMA (Seasonal ARIMA): This model is used to forecast sales by accounting for both trends and seasonality in the data.
        Process:
            Time-Series Analysis: Analyze historical sales data to identify trends and seasonal patterns.
            Model Configuration: Determine the ARIMA order (p, d, q) and seasonal order (P, D, Q, S) based on data's auto-correlation and partial auto-correlation plots.
            Training: Train the SARIMA model on historical data.
            Forecasting: Predict sales for future periods (e.g., 30 days) and evaluate the model using Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).

2. Profit Prediction Using Linear Regression

    Linear Regression: This model predicts profit based on features such as Research and Development (R&D) spending, marketing expenses, etc.
        Process:
            Data Preprocessing: Scale and select significant features using StandardScaler and Recursive Feature Elimination (RFE).
            Training: Train the linear regression model on the preprocessed data.
            Prediction: Use the model to predict profits and assess its accuracy using metrics like the coefficient of determination (R²) and MSE.
        Goal: Helps businesses allocate their budgets better by identifying which investments, such as R&D, drive profitability.

3. Revenue Prediction Using ARIMA

    ARIMA (Auto-Regressive Integrated Moving Average): Used for predicting revenue, particularly suitable for time-series financial data.
        Process:
            Time-Series Visualization: Use moving averages to observe trends and patterns.
            Model Configuration: Train the ARIMA model on historical revenue data.
            Forecasting: Predict revenue for future periods and store the results for further analysis.
        Application: Forecasts future revenue trends, allowing for proactive financial decision-making.

4. Price Optimization Using OLS (Ordinary Least Squares)

    OLS Regression: This model optimizes product pricing by analyzing the relationship between unit price and sales volume.
        Process:
            Data Analysis: Use sales data (product price, units sold) to create a regression model.
            Training: Train the model to predict the optimal price that maximizes sales volume.
            Optimization: Calculate the price point that will yield maximum revenue for each product category.
        Application: Provides businesses with data-driven pricing strategies to optimize revenue and remain competitive.

5. Customer Segmentation Using K-Means Clustering

    K-Means Clustering: This model segments customers based on their demographic and behavioral data.
        Process:
            Preprocessing: Encode categorical data like gender and country using OneHotEncoder.
            Cluster Determination: Use the Elbow Method to find the optimal number of clusters.
            Clustering: Group customers into segments based on their behaviors.
            Analysis: Analyze the mean values of key attributes within each segment to understand customer behavior.
        Goal: Helps businesses personalize marketing efforts, enhance customer engagement, and improve retention.

6. Streamlit Dashboard for Real-Time Interaction

    A Streamlit dashboard provides a user-friendly interface for interacting with these models. Business users can input relevant data (e.g., R&D spend, product categories) and receive real-time predictions through visualizations.


---

## 📸 Screenshots 

**The Streamlit Dashboard**
**Registration/Login**

![image](https://github.com/user-attachments/assets/5e92f86f-f214-4f15-9d0d-a380e7d093aa)

**Profit Prediction**

![image](https://github.com/user-attachments/assets/0b97038f-512e-46cb-ae9b-dac07cea9fa2)

**Revenue Prediction**

![image](https://github.com/user-attachments/assets/e123cba8-7c44-4fbc-b69b-2faf4fb8766a)


**Sales Prediction**

![image](https://github.com/user-attachments/assets/260047a7-2c7f-4f82-ac7d-f489cbd3e9ef)


**Customer Segmentation**

![image](https://github.com/user-attachments/assets/31db844a-86a7-44db-a5b9-2ffbdaf489d1)


**Price Optimization**

![image](https://github.com/user-attachments/assets/7da83e59-7a06-4df1-9be8-ca5b1875f838)


---

## ⚡ Getting Started  
### 1. Clone the Repository  
```bash
git clone https://github.com/Steive-URK21CS1188/enhancing-decision-making-with-ai-for-dynamic-business-insight-predictions.git
cd AI Business Insights
```
### 2. Start Application  
```bash
python -m streamlit run app.py
```

---

