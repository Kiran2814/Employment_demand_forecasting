# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:04:21 2021

@author: Kiran
"""

import streamlit as st
from analysis_functions import compare_industry, plot_industry, industry_preprocess, plot_volatility, compare_volatility

def compare(df):
    st.title('Compare Industries Growth')
    st.write("Here we are comparing and analyzing the trends in the different industries \
             and how they are affected by overall trends and seasonal trends. We can also\
            observe and compare the affects of economic recession and how the industries\
            responded and overcome that periods.")
    
    st.subheader('Select Two industries')
    industry_list = df['NOC'].tolist()
    industry_name_1 = st.selectbox("Select First Industry", (industry_list))
    industry_name_2 = st.selectbox('Select Second Industry', (industry_list))
    if industry_name_2 == industry_name_1:
        industry_data = industry_preprocess(df, 'January 1987', 'January 2021', industry_name_1)
        fig = plot_industry(industry_data)
        st.plotly_chart(fig, use_container_width=True)
        fig2 = plot_volatility(df, 'January 1987', 'January 2021', industry_name_1)
        st.plotly_chart(fig2, use_container_width=True)
    else:
        fig1 = compare_industry(df, 'January 1987', 'January 2021', industry_name_1, industry_name_2)
        st.plotly_chart(fig1, use_container_width=True)
        fig2 = compare_volatility(df, 'January 1987', 'January 2021', industry_name_1, industry_name_2)
        st.plotly_chart(fig2, use_container_width=True)