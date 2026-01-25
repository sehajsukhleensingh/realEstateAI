import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import seaborn as sns 
import matplotlib.pyplot as plt
import requests
import json

st.set_page_config(
    page_title = 'analytics'
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

url = "http://127.0.0.1:8000/analytics/sectorwise-price"
response = requests.get(url)
data = response.json()
data = pd.DataFrame(data)

st.header('Sectorwise Price per Sqft')
fig = px.scatter_mapbox( data , lat="latitude", lon="longitude",hover_name='sector',color="pricePerSqft", size="builtup",
                  color_continuous_scale=px.colors.cyclical.IceFire,  size_max=15, zoom=10 , mapbox_style="open-street-map")

st.plotly_chart(fig)


st.header('Area v/s Price')
key = st.selectbox('Property Type' , ['flat' , 'independent house'])
url = "http://127.0.0.1:8000/analytics/area-v-price"
response = requests.get(url,params={"flag":key})
data = pd.DataFrame(response.json())


fig = px.scatter(data , x = "builtup area (in sq feet)" , y = "price (in crores)" , color  = "builtup area (in sq feet)",
                    labels={
                        "price (in crores)":'Price (in crores)',
                        "builtup area (in sq feet)":'Area (in sqft)'
                    })
st.plotly_chart(fig)



st.header('Average number of Bedrooms')
key = st.selectbox('Property Type' , ['flat' , 'independent house' , 'overall'])
url = "http://127.0.0.1:8000/analytics/average-bedrooms"
response = requests.get(url,params={"flag":key})
data = response.json()
data = pd.DataFrame({"BHK":data.keys(),"bedRooms":data.values()})

fig = px.pie(data,values="bedRooms",names='BHK')
st.plotly_chart(fig)



st.header('Average Price (BHK)')
url = "http://127.0.0.1:8000/analytics/average-price-bhk"
response = requests.get(url)
data = response.json()
data = pd.DataFrame(data)

st.plotly_chart(px.box(data , x = 'bedRooms' , y = 'Y' , labels = {
    "Y" :"Price (in crores)",
    'bedRooms':'Bedrooms'
} ))


st.header('Distribution plot (Flats v/s Independent House)')
url = "http://127.0.0.1:8000/analytics/prices-range"
response = requests.get(url)
data = response.json()

fig , ax= plt.subplots()
sns.histplot(data["flats"],kde = True , label = 'Flat' )
sns.histplot(data["houses"], kde = True , label = "Independent House" , alpha = 0.3)
plt.xlabel('Price(in crores)')
plt.legend()
st.pyplot(fig)