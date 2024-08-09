# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:29:04 2024

@author: SAIL
"""

import pandas as pd
import store_home, store_dataOverview, store_Univariate, store_Bivariate, store_ml 
import streamlit as st


# Set the maximum number of columns to a large value
pd.options.display.max_info_columns = 50
#read dataset






def my_data():
    df = pd.read_excel("C:/Users/SAIL/Super_store/SuperStoreUS-2015.xlsx")
    return df


st.sidebar.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 20px;
    }
    </style>""", unsafe_allow_html=True)



# Create a menu
st.sidebar.title("Prioritizing Orders for Success")









# Add buttons to navigate between pages
if st.sidebar.button('Home'):
    st.session_state.page = 'store_home'
if st.sidebar.button('Univariate Statistics'):
    st.session_state.page = 'store_Univariate'
if st.sidebar.button('Bivariate Statistics'):
    st.session_state.page = 'store_Bivariate'
if st.sidebar.button('Machine Learning Models'):
    st.session_state.page = 'store_ml'

# Display the selected page
if 'page' not in st.session_state:
    st.session_state.page = 'store_home'
if st.session_state.get('page') == 'store_home':
    store_home.main()
elif st.session_state.get('page') == 'store_Univariate':
    store_Univariate.main()
elif st.session_state.get('page') == 'store_Bivariate':
    store_Bivariate.main()
elif st.session_state.get('page') == 'store_ml':
    store_ml.main()