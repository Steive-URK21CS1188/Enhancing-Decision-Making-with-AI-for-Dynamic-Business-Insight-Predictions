import streamlit as st
import json
import os
import re
import string
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
session_state = st.session_state
if "user_index" not in st.session_state:
    st.session_state["user_index"] = 0

def signup(json_file_path="data.json"):
    st.title("Signup Page")
    with st.form("signup_form"):
        st.write("Fill in the details below to create an account:")
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        age = st.number_input("Age:", min_value=0, max_value=120)
        sex = st.radio("Sex:", ("Male", "Female", "Other"))
        password = st.text_input("Password:", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")

        if st.form_submit_button("Signup"):
            if password == confirm_password:
                user = create_account(name, email, age, sex, password, json_file_path)
                session_state["logged_in"] = True
                session_state["user_info"] = user
            else:
                st.error("Passwords do not match. Please try again.")

def check_login(username, password, json_file_path="data.json"):
    try:
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        for user in data["users"]:
            if user["email"] == username and user["password"] == password:
                session_state["logged_in"] = True
                session_state["user_info"] = user
                st.success("Login successful!")
                return user

        st.error("Invalid credentials. Please try again.")
        return None
    except Exception as e:
        st.error(f"Error checking login: {e}")
        return None
def initialize_database(json_file_path="data.json"):
    try:
        # Check if JSON file exists
        if not os.path.exists(json_file_path):
            # Create an empty JSON structure
            data = {"users": []}
            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file)
    except Exception as e:
        print(f"Error initializing database: {e}")
        
def create_account(name, email, age, sex, password, json_file_path="data.json"):
    try:
        # Check if the JSON file exists or is empty
        if not os.path.exists(json_file_path) or os.stat(json_file_path).st_size == 0:
            data = {"users": []}
        else:
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

        # Append new user data to the JSON structure
        user_info = {
            "name": name,
            "email": email,
            "age": age,
            "sex": sex,
            "password": password,

        }
        data["users"].append(user_info)

        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        st.success("Account created successfully! You can now login.")
        return user_info
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        st.error(f"Error creating account: {e}")
        return None

def login(json_file_path="data.json"):
    st.title("Login Page")
    username = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    login_button = st.button("Login")

    if login_button:
        user = check_login(username, password, json_file_path)
        if user is not None:
            session_state["logged_in"] = True
            session_state["user_info"] = user
        else:
            st.error("Invalid credentials. Please try again.")

def get_user_info(email, json_file_path="data.json"):
    try:
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
            for user in data["users"]:
                if user["email"] == email:
                    return user
        return None
    except Exception as e:
        st.error(f"Error getting user information: {e}")
        return None


def render_dashboard(user_info, json_file_path="data.json"):
    try:
        st.title(f"Welcome to the Dashboard, {user_info['name']}!")
        st.subheader("User Information:")
        st.write(f"Name: {user_info['name']}")
        st.write(f"Sex: {user_info['sex']}")
        st.write(f"Age: {user_info['age']}")

    except Exception as e:
        st.error(f"Error rendering dashboard: {e}")
   
def find_optimal_price(data, model, category, quantity):
    """
    Finds the optimal price for a given product category and quantity.

    Args:
    - data (DataFrame): The DataFrame containing the unit price data.
    - model: The pre-trained model for the selected product category.
    - category (str): The selected product category.
    - quantity (int): The desired quantity of the product.

    Returns:
    - dict: A dictionary containing the category and the optimal price for the given quantity.
    """
    start_price = data['unit_price'].min()
    end_price = data['unit_price'].max() * 1.1

    # Calculate the optimal price based on the model coefficients
    coef = model.params['unit_price']
    intercept = model.params['const']
    optimal_price = (quantity * coef) + intercept

    return {'category': category, 'Price': optimal_price}
def predict_customer_segment(model, country, gender):
    # Assuming model.predict takes features as input and returns the predicted segment
    features = [country, gender]  # Assuming these are the features your model expects
    predicted_segment = model.predict(features)
    return predicted_segment

                      
def main(json_file_path="data.json"):
    # alert_style = """
    # <style>
    #     .alert {
    #         padding: 10px;
    #         margin-bottom: 10px;
    #         border-radius: 5px;
    #         color: white;
    #         font-weight: bold;
    #         text-align: center;
    #     }
    #     .alert-success {
    #         background-color: #28a745;
    #     }
    #     .alert-danger {
    #         background-color: #dc3545;
    #     }
    # </style>
    #    """
    # st.markdown(
    #     """
    #     <style>
    #     body {
    #         color: red;
    #         background-color: #333333;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    # Set the background image
    # st.markdown(
    #     """
    #     <style>
    #     .stApp {
    #         background: url("https://wallpapercave.com/wp/wp2836001.jpg");
    #         background-size: cover;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    # st.markdown(alert_style, unsafe_allow_html=True)

    st.sidebar.title("AI Generated Business Insights")
    page = st.sidebar.radio(
        "Go to",
        ("Signup/Login", "Dashboard","Profit Prediction","Revenue Prediction","Sales Prediction",'Customer Segmentation','Price Optimization'),
        key="AI Business Insights",
    )

    if page == "Signup/Login":
        st.title("Signup/Login Page")
        login_or_signup = st.radio(
            "Select an option", ("Login", "Signup"), key="login_signup"
        )
        if login_or_signup == "Login":
            login(json_file_path)
        else:
            signup(json_file_path)

    elif page == "Dashboard":
        if session_state.get("logged_in"):
            render_dashboard(session_state["user_info"])
        else:
            st.warning("Please login/signup to view the dashboard.")

    elif page == "Profit Prediction":
        if session_state.get("logged_in"):
            st.title("Profit Prediction")
            st.write('Enter Your Inputs Here:')
            features = ['R&D Spend']
            a=[]
            RD_Expense = st.number_input('R& D Expense by the company : ')
          
        
            a=[RD_Expense]
            data = pd.DataFrame([a], columns=features)
            
            sc =StandardScaler()
            sc.fit_transform(data[['R&D Spend']])
        
            if st.button("Submit"):
                with open('profit_prediction.pkl', 'rb') as f:
                    model = pickle.load(f)
                y=model.predict(data)
                profit_prediction = y[0] 
                st.write(f"<h4 style='color:blue;'>Expected Profit :</h4> <p style='font-size:24px; color:green;'>${profit_prediction:.2f}</p>", unsafe_allow_html=True)
               
        else:
            st.warning("Please login/signup to use the App!!!")
    elif page == "Price Optimization":
        if session_state.get("logged_in"):
            st.title("Price Optimization")
            price_data = pd.read_csv('retail_price.csv')
            categories = price_data['product_category_name'].unique()
            selected_category = st.selectbox('Select Category', categories)

            # Filter data based on selected category
            category_data = price_data[price_data['product_category_name'] == selected_category]

            # Define exogenous variables (exog) based on the selected category data
            exog = sm.add_constant(category_data[['unit_price']])

            # Train a linear regression model
            model = sm.OLS(category_data['qty'], exog).fit()

            quantity = st.slider('Select Quantity', min_value=1, max_value=100, value=50)

            if st.button("Submit"):
                # Find optimal price for the selected category and quantity
                optimal_price = find_optimal_price(category_data, model, selected_category, quantity) 
                if optimal_price['Price'] < 0:
                    optimal_price['Price'] = abs(optimal_price['Price'])   
                st.write(f"<h5 style='color:blue;'>Product Category:</h5> <p style='font-size:18px; color:green;'>{optimal_price['category']}</p>", unsafe_allow_html=True)
                st.write(f"<h5 style='color:blue;'>Optimal Price for the selected quantity :</h5> <p style='font-size:18px; color:green;'>{optimal_price['Price']}</p>", unsafe_allow_html=True)
        else:
            st.warning("Please login/signup to use the App!!!")
    elif page == "Sales Prediction":
        if session_state.get("logged_in"):
            st.title("Sales Prediction")

            forecast_data = pd.read_csv('sales_forecast.csv')

        
            selected_date = st.selectbox('Select Date', forecast_data['Date'].unique())

            
            selected_prediction = forecast_data[forecast_data['Date'] == selected_date]['Forecasted Sales'].values[0]

            
            st.markdown(
                f"""
                <div style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; background-color: #f8f9fa;">
                    <h3 style="color: #007bff;">The predicted sales for {selected_date} is:</h3>
                    <p style="font-size: 24px; color: #28a745;">{selected_prediction}</p>
                </div>
                """
            ,unsafe_allow_html=True)
        else:
    
            st.warning("Please login/signup to use the App!!!")
    elif page == "Revenue Prediction":
        if session_state.get("logged_in"):
            st.title("Revenue Prediction")
            revenue_data = pd.read_csv('revenue_predictions.csv')


            selected_year = st.selectbox("Select Year", revenue_data["Year"].unique())

            # Display the revenue for the selected year
            selected_revenue = revenue_data.loc[revenue_data["Year"] == selected_year, 'Revenue Prediction'].values[0]
            st.markdown(
            f'<div style="font-size: 24px; color: #3366ff;; font-family: Arial, sans-serif;">'
            f'Revenue for <span style="color: #3366ff;">{selected_year}</span>: '
            f'<span style="color: #33cc33;">${selected_revenue:.2f}</span>'
            '</div>',
            unsafe_allow_html=True
        )
        else:
            st.warning("Please login/signup to use the App!!!")
    elif page == 'Customer Segmentation':
        if session_state.get("logged_in"):
            st.title("Customer Segmentation")
            
            with open('unique_countries.txt', 'r') as file:
                countries = file.read().splitlines()

            selected_country = st.selectbox('Select Country', countries)

            with open('unique_genders.txt', 'r') as file:
                genders = file.read().splitlines()

            # Dropdown for gender selection
            selected_gender = st.selectbox('Select Gender', genders)

            # Create a DataFrame with the selected country and gender
            data = pd.DataFrame({'gender': [selected_gender], 'country': [selected_country]})
            
            # Load the OHE object from the pickle file
            with open('ohe.pkl', 'rb') as f:
                ohe = pickle.load(f)
            
            # Apply the OHE transformation to the input data
            data_ohe = ohe.transform(data)

      
            with open('customer_segmentation.pkl', 'rb') as f:
                model = pickle.load(f)

            # Make a prediction using the model
            predicted_segment = model.predict(data_ohe)
            if st.button("Submit"):
                category = 'Category A' if predicted_segment == 0 else 'Category B'


                st.markdown(f"### Predicted Segment\n\n**Category:** {category}")
        else:
            st.warning("Please login/signup to use the App!!!")
    else:
        st.warning("Please login/signup to use the App!!!")
            
   


if __name__ == "__main__":
    initialize_database()
    main()
