import pandas as pd
from src.logger import logger

def load_data(path):

    try:
        df = pd.read_csv(path)
        logger.info("Dataset loaded successfully")
        return df

    except Exception as e:
        logger.error("Error loading dataset")
        raise e