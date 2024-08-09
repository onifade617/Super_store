# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:25:27 2024

@author: SAIL
"""

import pandas as pd
import streamlit as st

df = pd.read_excel("C:/Users/SAIL/Super_store/SuperStoreUS-2015.xlsx")

def main():
    st.title("Data Overview")
    st.write(df)