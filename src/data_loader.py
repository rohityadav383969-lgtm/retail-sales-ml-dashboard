'''import pandas as pd
import os

def load_data():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_path = os.path.join(base_dir, "data", "retail_sales_dataset.csv")

    df = pd.read_csv(data_path)
    df.columns = df.columns.str.lower().str.strip()

    return df'''

import pandas as pd
from src.logger import logger

def load_data(path):

    try:
        df = pd.read_csv("/Users/rohityadav/Desktop/sales_ml_project copy/data/retail_sales_dataset.csv")
        logger.info("Dataset loaded successfully")
        return df

    except Exception as e:
        logger.error("Error loading dataset")
        raise e