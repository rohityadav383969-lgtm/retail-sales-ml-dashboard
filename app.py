import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.eda import sales_by_category, gender_distribution, age_distribution
from src.regression import train_model, load_model, compare_models

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Retail Sales ML Dashboard", layout="wide")

# ---------------- LOAD DATA ----------------
df = load_data("data/retail_sales_dataset.csv")
df = clean_data(df)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Dashboard Menu")
menu = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Dataset",
        "EDA Analysis",
        "Model Comparison",
        "Regression Prediction"
    ]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.title("Retail Sales Data Science Project")
    st.write("This dashboard analyzes retail sales data and predicts sales using Machine Learning.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(df))
    col2.metric("Unique Categories", df["Product Category"].nunique())
    col3.metric("Average Age", int(df["Age"].mean()))

# ---------------- DATASET ----------------
elif menu == "Dataset":
    st.title("Dataset")
    st.dataframe(df)
    st.write("Dataset Shape:", df.shape)

# ---------------- EDA ----------------
elif menu == "EDA Analysis":
    st.title("Exploratory Data Analysis")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales by Category")
        fig1 = sales_by_category(df)
        st.pyplot(fig1)

    with col2:
        st.subheader("Gender Distribution")
        fig2 = gender_distribution(df)
        st.pyplot(fig2)

    st.subheader("Age Distribution (Interactive)")
    fig = px.histogram(df, x="Age", title="Age Distribution")
    st.plotly_chart(fig)

# ---------------- MODEL COMPARISON ----------------
elif menu == "Model Comparison":
    st.title("Machine Learning Model Comparison")
    results = compare_models(df)
    
    models = list(results.keys())
    scores = list(results.values())
    best_model = max(results, key=results.get)

    st.success(f"Best Performing Model: {best_model}")

    fig = px.bar(
        x=models,
        y=scores,
        title="Model Performance Comparison",
        labels={"x": "Model", "y": "R2 Score"},
        color=scores
    )
    st.plotly_chart(fig)

# ---------------- REGRESSION ----------------
elif menu == "Regression Prediction":
    st.title("Sales Prediction Model")
    model, score = train_model(df)

    st.success(f"Model Accuracy (R2 Score): {score:.2f}")
    st.markdown("---")
    st.subheader("Predict Sales")

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", 18, 80)
    with col2:
        quantity = st.number_input("Quantity", 1, 10)
    with col3:
        price = st.number_input("Price per Unit", 1)

    if st.button("Predict"):
        model = load_model()
        prediction = model.predict([[age, quantity, price]])
        
        st.success(f"Predicted Sales Amount: {prediction[0]:.2f}")

        fig, ax = plt.subplots()
        ax.bar(["Prediction"], [prediction[0]])
        ax.set_title("Sales Prediction")
        ax.set_ylabel("Amount")
        st.pyplot(fig)
