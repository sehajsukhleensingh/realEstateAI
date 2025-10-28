import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
import seaborn as sns 
import pickle 
import streamlit as st
import ast
import regex as re
st.markdown(
    """
    <style>
      
    /* Sidebar - frosted glass dark */
    [data-testid="stSidebarContent"] {
        background: rgba(40, 40, 60, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 12px;
        padding: 15px;
    }

    /* Sidebar nav items */
    [data-testid="stSidebarNavItems"] span {
        color: #E0E0E0 !important;
        font-family: 'Courier New', monospace !important;
        font-weight: 500;
    }
    [data-testid="stSidebarNavItems"] span:hover {
        color: #FFD369 !important;
        cursor: pointer;
    }
     [data-testid=stTable] td , [data-testid = stTable] th{
    font-family:courier;
    }
    [data-testid="stApp"] p,
    [data-testid="stApp"] h1,
    [data-testid="stApp"] h2,
    [data-testid="stApp"] h3,
    [data-testid="stApp"] span,
    [data-testid="stApp"] label,
    [data-baseweb="select"] div,
    input,
    button,
    [data-testid="stTable"] td,
    [data-testid="stTable"] th{
    font-family: courier !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
  
dt = pd.read_csv('website/datasets/flat-recomendations.csv')


from sklearn.feature_extraction.text import TfidfVectorizer

vectoriser = TfidfVectorizer()
vecMatrix = vectoriser.fit_transform(dt['features']) 

from sklearn.metrics.pairwise import cosine_similarity

cosSimFet = cosine_similarity(vecMatrix)

vecMat = vectoriser.fit_transform(dt['nearbyLocation'])

cosSimLoc = cosine_similarity(vecMat)


from sklearn.preprocessing import StandardScaler
obj = StandardScaler()

var = obj.fit_transform(dt[['price']])

from sklearn.metrics import pairwise_distances

dist = pairwise_distances(var,metric = 'euclidean')
# this calculated the euclidean distance of each value with all the others 

#  similarity = 1 - ( distance / max distance )

matSimPrice = 1 - ( dist / dist.max() )


def recomender(flatName , priceWeight ,featureWeight , locationWeight):

    if flatName not in dt['flatName'].values:
        return "flat not present in dataset"
    else:
    
        total = priceWeight + featureWeight + locationWeight
        
        finalSimScore = (priceWeight/total)*matSimPrice + (featureWeight/total)*cosSimFet + (locationWeight/total)*cosSimLoc
        
        indx = dt[dt['flatName'] == flatName].index[0]
        scores = list(enumerate(finalSimScore[indx]))

        scoresSorted = sorted(scores , key = lambda x:x[1]  , reverse = True)
        scoresSorted = scoresSorted[1:6]

        lis = []
        for index , score in scoresSorted:
            flat = {
                "name":dt.iloc[index]['flatName'],
                "simScore":round(score,2),
                "nearby locations":dt.iloc[index]['nearbyLocation'],
                "link":dt.iloc[index]['links']
            }
            lis.append(flat)

    return lis 

num = st.selectbox('Select / Type the sector number ' , sorted(dt['sector'].unique()))

def secNum(num):
    data = dt[dt['sector'] == num]['flatName']
    if data.empty:
        return f"There is no flat in sector : {num}"
    else:
        return data.values
    
flatName = st.radio("The Properties : " , options = secNum(num))

recomendations = recomender(flatName,0.8,0.5,0.7)
if isinstance(recomendations,list):
    st.table(pd.DataFrame(recomendations))
else:
    st.write("Flat not present in dataset")
    
