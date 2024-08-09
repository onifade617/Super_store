# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:25:27 2024

@author: SAIL
"""

import pandas as pd
import streamlit as st

df = pd.read_csv("SuperStoreUS-2015.csv")

def main():
    st.title("Data Overview")
    
