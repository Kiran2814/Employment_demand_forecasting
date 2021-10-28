# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:03:58 2021

@author: Kiran
"""

import plotly.express as px
from analysis_functions import load_and_clean, industry_preprocess, plot_industry, plot_volatility
from functions_eda_charts import plot_gender, plot_labour, plot_map
import pandas as pd
import streamlit as st

def analysis(df_t, df_c):
    st.title('Explore an Industry')
    
    #df = pd.read_csv('Data/employment3.csv', skiprows=8)
    industry_list = df_t['NOC'].tolist()
   
    #about total employment
   
    industry_name = st.selectbox("Select Industry", (industry_list))
    industry_data = industry_preprocess(df_t, 'January 1987', 'January 2021', industry_name)
    
    col1, col2 = st.beta_columns((1.75, 0.95))
    fig = plot_industry(industry_data)
    col1.plotly_chart(fig, use_container_width=False, config=({'displayModeBar': False})) 
    
    fig3 = plot_gender(df_c, industry_name)
    col2.plotly_chart(fig3, use_container_width=False, config=({'displayModeBar': False}))
    
    col3, col4 = st.beta_columns((1,0.6))
     
    fig2 = plot_volatility(df_t, 'January 1987', 'January 2021', industry_name)
    col3.plotly_chart(fig2, use_container_width=False, config=({'displayModeBar': False}))
    
    fig4 = plot_labour(df_c, industry_name)
    col4.plotly_chart(fig4, config=({'displayModeBar': False}))
    
    
    fig5 = plot_map(df_c, industry_name)
    st.plotly_chart(fig5, use_container_width=True, config=({'displayModeBar': False}))
    
    

    