import streamlit as st 
import pandas as pd
import numpy as np 

st.set_page_config(
    page_title = 'insights'
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
dt = pd.read_csv('website/datasets/Coef-Weights.csv')

st.header('Check how much the price increases approximately on average on increase in any of this feature ')

label = st.selectbox('Select the Feature' ,['Area' , 'Bed Room + Bath Room' , 'Balcony' , 'Servant Room'])

if label == 'Area':
    val = st.selectbox('number (sq. ft)',range(100,100000,100))

    coef = abs(dt[dt['features'] == 'builtup']['coef'].values[0])
    out = coef*10000000*val

    st.write(f"The price of the property increases approximately by {round(out,2)} rupees")

elif label == 'Balcony':

    val = st.selectbox('number',range(1,7))

    coef = abs(dt[dt['features'] == 'balcony']['coef'].values[0])
    out = coef*10000000*val

    st.write(f"The price of the property increases approximately by {round(out,2)} rupees")

else :
    val = st.selectbox('number',range(1,16))

    if label == 'Bed Room + Bath Room':

        coef1 = abs(dt[dt['features'] == 'bedRooms']['coef'].values[0])
        coef2 = abs(dt[dt['features'] == 'bathRooms']['coef'].values[0])
        out = (coef1+coef2)*10000000*val

        st.write(f"The price of the property increases approximately by {round(out,2)} rupees")

    else:

        coef = abs(dt[dt['features'] == 'servant room']['coef'].values[0])
        out = coef*10000000*val

        st.write(f"The price of the property increases approximately by {round(out,2)} rupees")



