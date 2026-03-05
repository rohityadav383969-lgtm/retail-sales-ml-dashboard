'''import pandas as pd

def clean_data(df):
    # 1️⃣ Standardize column names
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )

    # 2️⃣ Date conversion (safe)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 3️⃣ Feature engineering
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    return df'''
from src.logger import logger

def clean_data(df):

    try:

        df = df.drop_duplicates()

        df = df.dropna()

        logger.info("Data cleaned successfully")

        return df

    except Exception as e:

        logger.error("Error during data cleaning")

        raise e