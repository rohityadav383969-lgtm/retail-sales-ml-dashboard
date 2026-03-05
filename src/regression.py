import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor


# ---------------- TRAIN MODEL ---------------- #

def train_model(df):

    X = df[["Age","Quantity","Price per Unit"]]
    y = df["Total Amount"]

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = LinearRegression()

    model.fit(X_train,y_train)

    predictions = model.predict(X_test)

    score = r2_score(y_test,predictions)

    # auto create models folder
    os.makedirs("models", exist_ok=True)

    joblib.dump(model,"models/sales_model.pkl")

    return model,score


# ---------------- LOAD MODEL ---------------- #

def load_model():

    model = joblib.load("models/sales_model.pkl")

    return model


# ---------------- MODEL COMPARISON ---------------- #

def compare_models(df):

    X = df[["Age","Quantity","Price per Unit"]]
    y = df["Total Amount"]

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(),
        "XGBoost": XGBRegressor()
    }

    results = {}

    for name,model in models.items():

        model.fit(X_train,y_train)

        preds = model.predict(X_test)

        score = r2_score(y_test,preds)

        results[name] = score

    return results