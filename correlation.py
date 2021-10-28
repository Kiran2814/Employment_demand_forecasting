# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:04:40 2021

@author:Kiran
"""
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def correlation(df):
    
    st.title('Correlations between industries')
    industry_list = df['NOC'].tolist()
    st.subheader("Select multiple Industries:")
    
    df_trans = df.T
    df_trans.columns = df_trans.iloc[0]
    df_trans.drop(df_trans.index[0], inplace= True)
    for i in df_trans.columns:
        if i!= 'NOC':
            df_trans[i]=df_trans[i].astype(float)

    corr = df_trans.corr()
    #select radio
    kot = st.radio('Select the correlation level', ('All','Extremely Negative', 'Negative', 'Positive', 'Extremely Positive', 'Selective'))
    
    def coorelation_plot(df_trans,corr,kot):
        if kot == "All":
            fig = plt.figure(figsize=(12,8))
            sns.heatmap(corr, cmap="BrBG")
            st.pyplot(fig)
            
        if kot == "Extremely Negative":
            corr_en = corr[corr<= -0.7]
            corr_en = corr_en.dropna(axis=0, how='all')
            corr_en = corr_en.dropna(axis=1, how='all')
            fig = plt.figure(figsize=(12,8))
            sns.heatmap(corr_en, cmap="BrBG")
            st.pyplot(fig)
            
        if kot == 'Negative':
            corr_n = corr[corr > -0.7]
            corr_n = corr_n[corr_n <= -0.3]
            corr_n = corr_n.dropna(axis=0, how='all')
            corr_n = corr_n.dropna(axis=1, how='all')
            fig = plt.figure(figsize=(12,8))
            sns.heatmap(corr_n, cmap='BrBG')
            st.pyplot(fig)
            
        if kot == 'Positive':
            corr_p = corr[corr >= 0.4]
            corr_p = corr_p[corr_p <= 0.8]
            corr_p = corr_p.dropna(axis=0, how='all')
            corr_p = corr_p.dropna(axis=1, how='all')
            fig = plt.figure(figsize=(12,8))
            sns.heatmap(corr_p, cmap='BrBG')
            st.pyplot(fig)
        
        if kot == 'Extremely Positive':
            corr_ep = corr[corr > 0.8]
            corr_ep = corr_ep[corr_ep <= 1]
            corr_ep = corr_ep.dropna(axis=0, how='all')
            corr_ep = corr_ep.dropna(axis=1, how='all')
            fig = plt.figure(figsize=(12,8))
            sns.heatmap(corr_ep, cmap='BrBG')
            st.pyplot(fig)
        
        if kot == 'Selective':
            options = st.multiselect('Select various industries (at least 2)', (industry_list))
            if len(options) != 1:  
                try:
                    df_trans = df_trans[df_trans.columns[df_trans.columns.isin(options)]]
                    corr = df_trans.corr()
                    fig = plt.figure(figsize=(12,8))
                    sns.heatmap(corr, cmap='BrBG', annot=True)
                    st.pyplot(fig)
                except:
                    pass
            else:
                st.write('Only one industry is selected. Please select at least 2 industries for coorelation.')
          
    coorelation_plot(df_trans, corr, kot)