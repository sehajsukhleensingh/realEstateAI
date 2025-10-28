import streamlit as st
import pickle
import pandas as pd
import numpy as np 
import os
import pickle

# Always resolves path correctly no matter where Streamlit runs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "dt.pkl")  # file in the same folder as predictor

with open(MODEL_PATH, "rb") as file:
    dt = pickle.load(file)

PIPELINE_PATH = os.path.join(BASE_DIR, "pipeline.pkl")

with open(PIPELINE_PATH, "rb") as file:
    pipeline = pickle.load(file)

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
if propertyType == 'Flat':
    propertyType = 0.0
else:
    propertyType = 1.0

builtup = float(st.number_input('Builtup Area'))

bedRoom = float(st.selectbox('Bed Rooms',sorted(dt['bedRooms'].unique())))

bathRooms = float(st.selectbox('Bath Rooms',sorted(dt['bathRooms'].unique())))

agePosseesion = st.selectbox('Age Of Property',['new property','relatively new property','old property','moderately old property','under construction'])
if agePosseesion == 'new property':
    agePosseesion = 1.0
elif agePosseesion == 'relatively new property':
    agePosseesion = 3.0
elif agePosseesion == 'old property':
    agePosseesion = 2.0
elif agePosseesion == 'moderately old property':
    agePosseesion = 0.0
else:
    agePosseesion = 4.0

balcony = st.selectbox('Balcony',[0.0,1.0,2.0,3.0,'3+'])
if balcony == '3+':
    balcony = 4.0

pooja = st.selectbox('Pooja Room',[0.0,1.0])
servant = st.selectbox('Servant Room',[0.0,1.0])
study = st.selectbox('Study Room',[0.0,1.0])
store = st.selectbox('Store Room',[0.0,1.0])
other = st.selectbox('Other Utility Rooms',[0.0,1.0])

lux = st.selectbox('Luxury Preference',['Budget' ,'Semi Luxurious','Luxurious' ])
if lux == 'Budget':
    lux = 0.0
elif lux == 'Semi Luxurious':
    lux = 2.0
else:
    lux = 1.0

height = st.selectbox('Floor Preference',['Low Rise' , 'Mid Rise' , 'High Rise'])
if height == 'Low Rise':
    height = 1.0
elif height == 'Mid Rise':
    height = 2.0
elif height == 'High Rise':
    height = 0.0
else:
    height = 3.0

if st.button("Predict Price"):
    data = [sector,propertyType,builtup,bedRoom,bathRooms,agePosseesion,balcony,pooja,servant,study,other,store,lux,height]
    df = pd.DataFrame([data],columns = dt.columns)
   
    # prediction 
    base = round(np.expm1(pipeline.predict(df))[0],2)
    low = round(base - 0.33,2) 
    high = round(base + 0.33,2)

    st.write(f"The price of property is between {low} cr and {high} cr ")