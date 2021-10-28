# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:00:57 2021

@author:Kiran
"""

import streamlit as st

def insights():
    st.title('Key Insights.')
    
    st.write('The labour market of Canada has been increasing linearly throughout the years with seasonal swings in employment cycle.\
             Total Employment in Canada has increased by around 63% in 2019 from the year 1987, and 17% in just the last decade.\
             Being at its peak in 2019 with 19 million people actively employed, and after the covid-19 lockdown across the globe, the employmemt decreased by 18% just within 6 months.  \
            The Canadian market has come along facing two of the most difficult periods when the world was halted by a financial crisis (The Great Recession 2008) and\
            by a global pandemic (The Covid-19 Pandemic 2020).')
            
    st.write('The declining affects of The Great Recession is very low compared\
            to Covid Pandemic because during the time of Recession the cash cycle had stopped\
            and moving at very slow rates. Not many employees were fired or layed off, but they had major \
            salary cuts as the companies were not ready to roll the money in the chain. Hence it had very small change\
            in the job market, but it took longer time to catch the pace.')
    
    st.write('In Contrast, the Covid Pandemic was the opposite, where many companies had holded their productions,\
             warehouses, offices, etc. The companies which were majorly dependent on hand labour work suffered the\
            most in the lockdown. There were heavy layoffs in this industries as the production factories and\
            warehouses were closed. The Jobs which were able to transfer their staff to Work from Home, had seen\
            a much less layoffs and run their companies with closed doors. ')
    
    st.header('Growth of industries.')
    st.write("The growth of any industry always depends on the industry's share to the Nations GDP,\
             thier respective growth, Technological advancement, Domestics and Foreign investments, Government Policies and Government support.")
    st.write('**The most growing industries.**')
    st.write('1. Assisting occupations in support of health services (242 %)')
    st.write('2. Professional occupations in law and social, community and government services (231 %)')
    st.write('3. Professional occupations in natural and applied sciences (198 %)')
    
    st.write('**The least growing industries **')
    st.write('1. Workers in natural resources, agriculture and related production (-34 %)')
    st.write('2. Processing and manufacturing machine operators and related production workers (-25 %)')
    st.write('3. Office support occupations (-19 %)')
    
    st.header('Stability of Industries.')
    st.write("The Stability of any industry can also be analyzed by observing the volatility of the industry\
             \. This observation can let us know the seasonal redundancy of any industries, how offend a \
                 discharge or recruit occurs. ")
    st.write("**The Most Stable Industries are:**")
    st.write("1. Middle management occupations in trades, transportation, production and utilities.")
    st.write("2. Management occupations")
    st.write("3. Maintenance and equipment operation trades.")
    
    
    st.write("**The least stable industries are:**")
    st.write('1. Harvesting, landscaping and natural resources labourers')
    st.write('2. Assisting occupations in support of health services')
    st.write('3. Professional occupations in law and social, community and government services')
    
