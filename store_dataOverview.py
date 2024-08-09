# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:25:27 2024

@author: SAIL
"""

import pandas as pd
import streamlit as st


def main():
    st.title("Data Overview")
    df = pd.read_excel("C:/Users/SAIL/Super_store/SuperStoreUS-2015.xlsx")
    st.write(df)