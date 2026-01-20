import streamlit as st
import pickle
import pandas as pd
import numpy as np 
import os
import pickle
from core.config import ( P_LUX_MAP , P_AGE_MAP , P_HEIGHT_MAP , P_TYPE_MAP 
                         , P_UTITLITY_MAP , P_BALCONY_MAP )
from core.predictor import price_predictor


# Path of this file: website/pages/01-predictor.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up: pages → website → project root
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

DT_PATH = os.path.join(PROJECT_ROOT, "artifacts", "dt.pkl")

with open(DT_PATH, "rb") as file:
    dt = pickle.load(file)

st.set_page_config(
    page_title = 'predictor'
)
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

     div.stButton > button {
        background-color: #EAE7DC;
        color: #000 !important;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
        border: none;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #d4cfc4;
        cursor: pointer;
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

st.header("Enter Data ")

sector = st.selectbox('Sector',sorted(dt['sector'].unique()))

propertyType = st.selectbox('Property Type',['Flat' , 'Independent House'])
propertyType = P_TYPE_MAP[propertyType]

builtup = float(st.number_input('Builtup Area'))

bedRoom = float(st.selectbox('Bed Rooms',sorted(dt['bedRooms'].unique())))

bathRooms = float(st.selectbox('Bath Rooms',sorted(dt['bathRooms'].unique())))

agePosseesion = st.selectbox('Age Of Property',['new property','relatively new property','old property','moderately old property','under construction'])
agePosseesion = P_AGE_MAP[agePosseesion]

balcony = st.selectbox('Balcony',[0,1,2,3,'3+'])
balcony = P_BALCONY_MAP[balcony]

pooja = st.selectbox('Pooja Room',["no","yes"])
pooja = P_UTITLITY_MAP[pooja]

servant = st.selectbox('Servant Room',["no","yes"])
servant = P_UTITLITY_MAP[servant]

study = st.selectbox('Study Room',["no","yes"])
study = P_UTITLITY_MAP[study]

store = st.selectbox('Store Room',["no","yes"])
store = P_UTITLITY_MAP[store]

other = st.selectbox('Other Utility Rooms',["no","yes"])
other = P_UTITLITY_MAP[other]

lux = st.selectbox('Luxury Preference',['Budget' ,'Semi Luxurious','Luxurious' ])
lux = P_LUX_MAP[lux]

height = st.selectbox('Floor Preference',['Low Rise' , 'Mid Rise' , 'High Rise'])
height = P_HEIGHT_MAP[height]


if st.button("Predict Price"):
    data = [sector,propertyType,builtup,bedRoom,bathRooms,agePosseesion,balcony,pooja,servant,study,other,store,lux,height]
    df = pd.DataFrame([data],columns = dt.columns)
   
    # prediction 
    base = round(price_predictor(df),2)
    low = round(base - 0.33,2) 
    high = round(base + 0.33,2)

    st.write(f"The price of property is between {low} cr and {high} cr ")