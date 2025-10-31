import streamlit as st 

st.set_page_config(
    page_title = 'Home'
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
    /* Center content */
        .main {
            padding: 3rem 2rem;
        }

        /* Headings */
        h1, h2, h3 {
            color: #9AA2FF;  /* soft indigo tone */
            text-align: center;
        }

        /* Paragraphs */
        p {
            color: #D6D6D6;
            font-size: 1.1rem;
            line-height: 1.6;
            text-align: center;
        }

        /* How-to box styling */
        .how-to {
            background-color: #2A2B33;
            padding: 1.8rem;
            border-radius: 15px;
            margin-top: 2rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
            border: 1px solid #3C3C3C;
        }

        li {
            margin: 0.7rem 0;
            font-size: 1.05rem;
            color: #CFCFCF;
        }

        .highlight {
            color: white;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Real Estate Intelligence System")
st.markdown("### *Predict • Analyze • Recommend • Understand property trends*")

st.markdown("""
This platform helps users explore housing prices, analyze market trends, 
predict property values, and find similar listings based on your preferences.  
It brings together predictive modeling, analytics visualization, and intelligent 
recommendations to simplify real estate decision-making.
""")

# Divider
st.markdown("---")
st.markdown("## 💡 How to Use")

st.markdown("""
<div class="how-to">
    <ol>
        <li><span class="highlight">Go to Predictor →</span> Enter your property details (sector, area, bedrooms, bathrooms, etc.) to get the predicted price.</li>
        <li><span class="highlight">Check Analytics →</span> Explore market patterns sector-wise through interactive graphs showing price trends for flats and houses.</li>
        <li><span class="highlight">Use Recommender →</span> Provide a sector number or price to find nearby or similar flats.</li>
        <li><span class="highlight">Explore Insights →</span> Understand how property features like bedrooms, bathrooms, and area affect pricing.</li>
    </ol>
</div>
""", unsafe_allow_html=True)