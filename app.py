import streamlit as st
st.set_page_config(page_title='Demand Forecasting',layout="wide",initial_sidebar_state="expanded")
   
from PIL import Image
import home, analysis, compare, correlation, forecasting, insights
import pandas as pd
from analysis_functions import load_and_clean

#Title and title image


df_t = pd.read_csv('Data/employment3.csv', skiprows=8)
df_t = load_and_clean(df_t)

df_c = pd.read_csv('Data/data_cleaned.csv')


#Sidebar options

clg_logo = Image.open('image/StClair.png')
st.sidebar.image(clg_logo)

st.sidebar.title('Explore')
options = st.sidebar.radio('Select a page:', 
    ['Home', 'Key Insights', 'Industry Analysis', 'Compare Industries', 'Correlations', 'Forecasting'])

if options == 'Home':
    home.home()
if options == 'Key Insights':
    insights.insights()
if options == 'Industry Analysis':
    analysis.analysis(df_t, df_c)
if options == 'Compare Industries':
    compare.compare(df_t)
if options == 'Correlations':
    correlation.correlation(df_t)
if options == 'Forecasting':
    forecasting.forecasting(df_t)
st.sidebar.subheader('Team Members')
st.sidebar.write('* Priyank Patel (w0753860@myscc.ca)')
st.sidebar.write('* Nidhi Patel (w0749144@myscc.ca)')
