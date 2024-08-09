# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:25:41 2024

@author: SAIL
"""

import streamlit as st
import pandas as pd


df = pd.read_csv("SuperStoreUS-2015.csv")
df.columns
def main():
    st.title("Univariate Data Analysis")
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)
    col11, col12 = st.columns(2)
    col13, col14 = st.columns(2)
    col15, col16 = st.columns(2)
   
    
    
    with col3:
        st.header("Order Priority")
        # Count the occurrences of each category
        orderPriority_counts = df['Order Priority'].value_counts().reset_index()
        orderPriority_counts.columns = ['Order Priority', 'Count']
        
        st.bar_chart(pd.DataFrame(orderPriority_counts), x = 'Order Priority', y = 'Count')
    
    with col1:
        st.markdown("## Discount")
        # Count the occurrences of each category
        discount_counts = df['Discount'].value_counts().reset_index()
        discount_counts.columns = ['Discount', 'Count']
        st.line_chart(pd.DataFrame(discount_counts), x = 'Discount',  y = 'Count')
        
     
    with col2:
        st.header("Customer Name")
        # Count the occurrences of each category
        customerName_counts = df['Customer Name'].value_counts().reset_index()
        customerName_counts.columns = ['Customer Name', 'Count']
        
        st.bar_chart(pd.DataFrame(customerName_counts), x = 'Customer Name', y = 'Count')
        
        
    
        
    with col4:
        st.header("Ship Mode")
        # Count the occurrences of each category
        ship_counts = df['Ship Mode'].value_counts().reset_index()
        ship_counts.columns = ['Ship Mode', 'Count']
        
        st.bar_chart(pd.DataFrame(ship_counts), x = 'Ship Mode', y = 'Count')
        
    with col5:
        st.header("Customer Segment")
        # Count the occurrences of each category
        csegment_counts = df['Customer Segment'].value_counts().reset_index()
        csegment_counts.columns = ['Customer Segment', 'Count']
        
        st.bar_chart(pd.DataFrame(csegment_counts), x = 'Customer Segment', y = 'Count')
        
    with col6:
         st.header("Product Category")
         # Count the occurrences of each category
         pcategory_counts = df['Product Category'].value_counts().reset_index()
         pcategory_counts.columns = ['Product Category', 'Count']
         
         st.bar_chart(pd.DataFrame(pcategory_counts), x = 'Product Category', y = 'Count')
         
         
    with col7:
         st.header("Product Sub-Category")
         # Count the occurrences of each category
         pscategory_counts = df['Product Sub-Category'].value_counts().reset_index()
         pscategory_counts.columns = ['Product Sub-Category', 'Count']
         
         st.bar_chart(pd.DataFrame(pscategory_counts), x = 'Product Sub-Category', y = 'Count')
         
         
    with col8:
         st.header("Product Container")
         # Count the occurrences of each category
         container_counts = df['Product Container'].value_counts().reset_index()
         container_counts.columns = ['Product Container', 'Count']
         
         st.bar_chart(pd.DataFrame(container_counts), x = 'Product Container', y = 'Count')
         
    with col9:
         st.header("Opened File")
         # Count the occurrences of each category
         file_counts = df['Is opened?'].value_counts().reset_index()
         file_counts.columns = ['File', 'Count']
         
         st.bar_chart(pd.DataFrame(file_counts), x = 'File', y = 'Count')
         
         
    with col10:
         st.header("Product Name")
         # Count the occurrences of each category
         Pname_counts = df['Product Name'].value_counts().reset_index()
         Pname_counts.columns = ['Product Name', 'Count']
         
         st.bar_chart(pd.DataFrame(Pname_counts), x = 'Product Name', y = 'Count')
    
    with col11:
         st.header("Product Base Margin")
         # Count the occurrences of each category
         base_counts = df['Product Base Margin'].value_counts().reset_index()
         base_counts.columns = ['Product Base Margin', 'Count']
         
         st.bar_chart(pd.DataFrame(base_counts), x = 'Product Base Margin', y = 'Count')
         
         
    with col12:
         st.header("Country")
         # Count the occurrences of each category
         country_counts = df['Country'].value_counts().reset_index()
         country_counts.columns = ['Country', 'Count']
         
         st.bar_chart(pd.DataFrame(country_counts), x = 'Country', y = 'Count')
         
    with col13:
         st.header("Region")
         # Count the occurrences of each category
         region_counts = df['Region'].value_counts().reset_index()
         region_counts.columns = ['Region', 'Count']
         
         st.bar_chart(pd.DataFrame(region_counts), x = 'Region', y = 'Count')
         
    with col14:
         st.header("State or Province")
         # Count the occurrences of each category
         state_counts = df['State or Province'].value_counts().reset_index()
         state_counts.columns = ['State or Province', 'Count']
         
         st.bar_chart(pd.DataFrame(state_counts), x = 'State or Province', y = 'Count')
         
         
    with col15:
         st.header("City")
         # Count the occurrences of each category
         city_counts = df['City'].value_counts().reset_index()
         city_counts.columns = ['City', 'Count']
         
         st.bar_chart(pd.DataFrame(city_counts), x = 'City', y = 'Count')
         
         
    with col16:
         st.header("Postal Code")
         # Count the occurrences of each category
         city_counts = df['Postal Code'].value_counts().reset_index()
         city_counts.columns = ['Postal Code', 'Count']
         
         st.bar_chart(pd.DataFrame(city_counts), x = 'Postal Code', y = 'Count')
         
         
    
         
    
    