# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:02:20 2021

@author:Kiran
"""

import streamlit as st
from PIL import Image

def home():
    title_image = Image.open('image/for_hire.jpg')
    st.image(title_image, use_column_width=True)
    st.title('Employment Demand Forecasting in Canada')

    st.header('Introduction.')
    st.write('This is a research project, performed to analyze and forecast the employment demand for the\
             next decade in the industries classified under the NOC classification system. This forecasting\
            is done using Statistical models and Neural Network models trained using the official statistics\
            published by the Government. This forecast has two parts, without considering the events of 2020 and,\
            taking consideration of the recent Covid-19 pandemic and the stagflation that followed the lockdown.')
    st.write('This research can be further used for economic planning immigration plans, forming policies for\
             retirement and pension support, training regimes and skill acquisition according to industry standards.\
            The projection can also be used by companies to plan their investment in a high growing market where\
            they can find suitable skilled workers, revamping better career development.')
            
    st.header('Background.')
    st.write('After the COVID-19 Pandemic, the world is finally recovering to its former glory. The Most damaged\
             caused during the lockdown was on the worldwide job markets, estimated around 225 million job losses\
            all over the world. The Job market is now elevating after the vaccine is been distributed, but it\
            was one of worst crash the world has seen, more than The Great Recession of 2008.')
    st.write('Every Government in the world is trying to push their economy through increase in jobs and employments.\
             The Canadian Government is been very aggressive to their statement by inviting  400,000 immigrants each\
            year to increase their economy and reduce the employment gap in skilled workers.The Canadian government has\
            already started to implement the COVID-19 Economic Response plan to support canadian individual and businesses.')
    st.write('The goverment estimates that 40% of the total employment shares to professional, science and tech-related jobs\
             by the year 2025 according to The Innovation and Skills Plan. Also the government has annouced $10 billion in\
            new major infrastructure initiatives which would create about 60,000 jobs in immediate time.')
    #Dataset
    st.header('Dataset Source.')
    st.write('The Labour Force Survey (LFS) data is used in this research which is a measure of current state of\
             labour market by conducting monthly surveys by Statistic Canada. This Data is collected by mandatory\
            survey in 3rd week of every month and published early next month. It contains aggregated numbers of\
            national employment and unemployment. For the forecascifically\
            using data of national employment from January 1987 to January 2021 to consider the events of recent\
            pandemic. It contains data for NOC categories 00 to 96. Total 50 industries are classified under this.')
    st.markdown('Statistics Canada. *Table 14-10-02s96-01  Labour force characteristics by occupation, monthly, \
                unadjusted for seasonality (x 1,000)*, Date modified: 2021-03-20, DOI: https://doi.org/10.25318/1410029601-eng')
    
    st.header('Previous studies.')
    st.write('* The COPS model produced by Employment and Social Development for projections of 293 occupational\
             covering the entire workforces. This projections allows to analyze the labour storage and labour surplus of different occupations.')
    st.write('Statistics Canada,  *Canadian Occupational Projection System (COPS)*, Date modified:2017-10-03, http://professions.edsc.gc.ca/sppc-cops/w.2lc.4m.2@-eng.jsp')
    st.write('* The Forecast of Canadian Occupation Growth (FCOG) published by brookfield institude which used\
             600+ change signals in labour market integrating with experts insights to forecast if the industries are on trend to increase or decrease over time.')
    st.write('Brookfield Institude for institude + entrepreneurship, *Employment in 2030: Action Labs*, https://brookfieldinstitute.ca/employment-in-2030-action-labs/ ')
    st.write('* The Nesta.org has used a novel mixed method to map the employment changes and implications for skills. \
             The projection is done by identifying the bundles of skills, abilities, and knowledge that are likely to be important in future and skill investment having greatest impact on occupational demand.')
    st.write('Bakhsi, Hasan and Philippe Schnieder, *The Future of Skills: Employment in 2030*, 27 Sept. 2017, https://www.nesta.org.uk/report/the-future-of-skills-employment-in-2030/')
    