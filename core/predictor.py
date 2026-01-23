import pickle
import pandas as pd
import numpy as np
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances


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


def recommender_system(flat_name,price_weight,location_weight,features_weight):

    dt = pd.read_csv('src/data/final/flat-recomendations.csv')

    vectoriser = TfidfVectorizer()
    scaler = StandardScaler()
    
    location_vec = vectoriser.fit_transform(dt["nearbyLocation"])
    features_vec= vectoriser.fit_transform(dt['features'])
    prices_scaled = scaler.fit_transform(dt[['price']])

    location_cos_sim = cosine_similarity(location_vec)
    features_cos_sim = cosine_similarity(features_vec)

    distance = pairwise_distances(prices_scaled,metric="euclidean")
    # this calculated the euclidean distance of each value with all the others 
    #  similarity = 1 - ( distance / max distance )

    price_sim_score = 1 - (distance / distance.max())

    if flat_name not in dt["flatName"].values:
        raise ValueError("the flat name is not present")
    
    total_weight  = price_weight + location_weight + features_weight

    combined_cos_sim_score = (price_weight/total_weight)*price_sim_score +  (location_weight/total_weight)*location_cos_sim + (features_weight/total_weight)*features_cos_sim   
    
    dt_index = dt[dt["flatName"] == flat_name].index[0]

    flat_sim_scores = list(enumerate(combined_cos_sim_score[dt_index]))
    sorted_flat_sim_score = sorted(flat_sim_scores,key=lambda x : x[1] , reverse=True)

    top_recommendations = sorted_flat_sim_score[1:6]

    lis = []
    for index , score in top_recommendations:
        flat = {
            "name":dt.iloc[index]['flatName'],
            "simScore":round(score,2),
            "nearby locations":dt.iloc[index]['nearbyLocation'],
            "link":dt.iloc[index]['links']
            }
        lis.append(flat)

    return lis 