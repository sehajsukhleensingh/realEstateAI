import pickle
import pandas as pd
import numpy as np
import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "..", "artifacts")

PIPELINE_PATH = os.path.join(ARTIFACTS_DIR, "pipeline.pkl")
MODEL_VERSION = "1.0.0"

with open(PIPELINE_PATH, "rb") as file:
    pipeline = pickle.load(file)

def price_predictor(df : pd.DataFrame) -> int :
    """
    Docstring for price_predictor
    
    :param df: the dataframe of the values entered by the user 
    :type df: pd.DataFrame
    :return: it returns the predicted price of the property using the pipeline 
    :rtype: int
    """

    expected_cols = pipeline.feature_names_in_

    missing_cols = set(expected_cols) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing cols {missing_cols}")
    
    df = df[expected_cols] # enforcing the column order , even if they are correct 
    
    price = pipeline.predict(df)
    return np.expm1(price)[0]

