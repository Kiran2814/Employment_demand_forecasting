# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:05:13 2021

@author:Kiran
"""

import streamlit as st
import pickle
from statsmodels.tsa.statespace.sarimax import SARIMAX
from analysis_functions import plot_models, industry_preprocess, plot_forecasted

def forecasting(df):
    st.title('Forecasting Employment in Industries')
    
    st.subheader('Select an Industry to forecast')
    industry_list = df['NOC'].tolist()
    industry_name = st.selectbox('',(industry_list))
    fig = plot_forecasted(industry_name)
    st.plotly_chart(fig, use_container_width=True)
    st.write("**Disclaimer**: This forecast is an approximation based on statistical models using data from previous years\
             This forecast is an approximation based on statistical models using data from previous years.\
             It should be not considered as inevitable future. Employment demand is sensitive to Nations GDP,\
             their respective growth, Technological advancement, Domestics and Foreign investments, Government Policies and Government support.")
