# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:25:27 2024

@author: SAIL
"""

from store_main import my_data
import streamlit as st


def main():
    st.title("Data Overview")


    #import data frame
    df = my_data()
    st.write(df)