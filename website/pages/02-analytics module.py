import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import seaborn as sns 
import matplotlib.pyplot as plt

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

dt = pd.read_csv('datasets/dataset-v6.csv')
dt.drop(columns = 'Unnamed: 0' , inplace = True)

dt['pricePerSqft'] = round((dt['Y']*10000000)/dt['builtup'],2)

latLong = pd.read_csv('datasets/latlong.csv')

latLong['sector'] = latLong['sector'].astype('int')

temp = dt.merge(latLong,on='sector')

temp['latitude'] = temp['coordinates'].str.replace('N','').str.replace('E','').str.replace('°','').str.split(',').str[0]
temp['longitude'] = temp['coordinates'].str.replace('N','').str.replace('E','').str.replace('°','').str.split(',').str[1]

temp.drop(columns = 'coordinates' , inplace = True)

temp['latitude'] = temp['latitude'].astype('float')
temp['longitude'] = temp['longitude'].astype('float')

groupDt = temp.groupby('sector').mean()[['Y','pricePerSqft','builtup','latitude','longitude']].reset_index()

st.header('Sectorwise Price per Sqft')
fig = px.scatter_mapbox( groupDt, lat="latitude", lon="longitude",hover_name='sector',color="pricePerSqft", size="builtup",
                  color_continuous_scale=px.colors.cyclical.IceFire,  size_max=15, zoom=10 , mapbox_style="open-street-map")

st.plotly_chart(fig)

st.header('Area v/s Price')
key = st.selectbox('Property Type' , ['Flat' , 'Independent house'])
if key == 'Flat':

    fig = px.scatter(dt[dt['propertyType'] == 0.0] , x = 'builtup' , y = 'Y' , color  = 'builtup',
                    labels={
                        'Y':'Price (in crores)',
                        'builtup':'Area (in sqft)'
                    })

    st.plotly_chart(fig)
else:
    fig = px.scatter(dt[dt['propertyType'] == 1.0] , x = 'builtup' , y = 'Y' , color  = 'builtup',  
                    labels={
                        'Y':'Price (in crores)',
                        'builtup':'Area (in sqft)'
                    })

    st.plotly_chart(fig)


st.header('Average number of Bedrooms')
key = st.selectbox('Property Type' , ['Flat' , 'Independent house' , 'Overall'])

if key == 'Flat':
    fig = px.pie(dt[dt['propertyType'] == 0.0],names='bedRooms')
    st.plotly_chart(fig)
elif key == 'Independent house':
    fig = px.pie(dt[dt['propertyType'] == 1.0],names='bedRooms')
    st.plotly_chart(fig)
else:
    fig = px.pie(dt,names = 'bedRooms' )
    st.plotly_chart(fig)


st.header('Average Price (BHK)')

st.plotly_chart(px.box(dt[dt['bedRooms'] <= 5] , x = 'bedRooms' , y = 'Y' , labels = {
    "Y" :"Price (in crores)",
    'bedRooms':'Bedrooms'
} ))

st.header('Distribution plot (Flats v/s Independent House)')
fig , ax= plt.subplots()
sns.histplot(dt[dt['propertyType']==0.0]['Y'],kde = True , label = 'Flat' )
sns.histplot(dt[dt['propertyType'] == 1.0]['Y'] , kde = True , label = "Independent House" , alpha = 0.3)
plt.xlabel('Price(in crores)')
plt.legend()
st.pyplot(fig)