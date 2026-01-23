import pandas as pd
import streamlit as st
from core.predictor import recommender_system

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
  
dt = pd.read_csv('src/data/final/flat-recomendations.csv')

num = st.selectbox('Select / Type the sector number ' , sorted(dt['sector'].unique()))

def secNum(num):
    data = dt[dt['sector'] == num]['flatName']
    if data.empty:
        return f"There is no flat in sector : {num}"
    else:
        return data.values
    
flatName = st.radio("The Properties : " , options = secNum(num))


recomendations = recommender_system(flatName,0.8,0.5,0.7)
if isinstance(recomendations,list):
    st.table(pd.DataFrame(recomendations))
else:
    st.write("Flat not present in dataset")
    
