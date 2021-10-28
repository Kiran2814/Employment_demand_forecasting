## Importing all libraries necessary

import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import re
import itertools
import warnings
import pickle
from zipfile import ZipFile
from statsmodels.tsa.statespace.sarimax import SARIMAX
warnings.filterwarnings("ignore")

##All Functions


#For loading and cleaning data
def load_and_clean(df):
    df = df[0:52]
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.rename(columns={'National Occupational Classification (NOC) 6':'NOC'}, inplace=True)
    df['NOC'].replace({'Total, all occupations 7' : 'Total Employment'}, inplace=True)
    for i in df.columns:
        if i!= 'NOC':
            df[i]=df[i].apply(lambda x:x.replace(',',''))
            df[i]=df[i].astype(float)
    
    return df


#For plotting single industry
def plot_industry(industry):
    fig = px.line(
        industry,
        x=industry.index,
        y=industry.columns[0],
        title="Change in Employment (x1000)",
        labels = {'index':'Date',industry.columns[0]: 'Growth in Employment'}
    )
    fig.update_layout(height=500, width=750, autosize=True,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(count=5,
                     label="5y",
                     step="year",
                     stepmode="backward"),
                dict(count=10,
                     label="10y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    ))
    
    return fig


#For industry data preprocess
def industry_preprocess(df, start, end, industry):
    temp = df.copy()
    
    # selecting industry
    temp = temp[temp['NOC'] == industry].reset_index(drop=True)
    
    # Selecting time range
    temp = temp.loc[:, start:end]
    
    
    temp = temp.T.reset_index(drop=False)
    temp.columns=['time', industry]
    temp.index = pd.DatetimeIndex(temp.time.values, freq='infer')
    temp.drop('time', axis=1, inplace=True)
   
    return temp


## For comparing two industries plot
def compare_industry(df, start, end, industry1, industry2):
    industry_1 = industry_preprocess(df, start, end, industry1)
    industry_2 = industry_preprocess(df, start, end, industry2)
    
    industry_merged = industry_1.join(industry_2)
    # industry_merged.iloc[:, 1:3] = industry_merged.iloc[:, 1:3].astype(float)
    fig = px.line(industry_merged, 
                  x=industry_merged.index,
                  y=industry_merged.columns, 
                  labels = {'index':'Date','value': 'Growth in Employment', "variable":'Industry'}, 
                  title='Comparsion between ' + str(industry_merged.columns[0] + " & " + str(industry_merged.columns[1])
                  ))
    fig.update_layout(legend=dict(yanchor="bottom", y=0.90,xanchor="right", x=0.99),
                      xaxis=dict(
                            rangeselector=dict(
                                buttons=list([
                                    dict(count=6,
                                         label="6m",
                                         step="month",
                                         stepmode="backward"),
                                    dict(count=1,
                                         label="1y",
                                         step="year",
                                         stepmode="backward"),
                                    dict(count=5,
                                         label="5y",
                                         step="year",
                                         stepmode="backward"),
                                    dict(count=10,
                                         label="10y",
                                         step="year",
                                         stepmode="backward"),
                                    dict(step="all")
                                ])
                            ),
                            rangeslider=dict(
                                visible=True
                            ),
                            type="date"
    )
                     )
    return fig


#For comparing two volatitlity
def compare_volatility(df, start, end, industry1, industry2):
    industry_1 = industry_preprocess(df, start, end, industry1)
    industry_2 = industry_preprocess(df, start, end, industry2)
    industry_1v = industry_1.pct_change() * 100
    industry_2v = industry_2.pct_change() * 100
    industry_merged = pd.DataFrame(industry_1v).join(pd.DataFrame(industry_2v))
    # industry_merged.iloc[:, 1:3] = industry_merged.iloc[:, 1:3].astype(float)
    fig = px.line(industry_merged, 
                  x=industry_merged.index,
                  y=industry_merged.columns, 
                  labels = {'index':'Date','value': 'Stability in Industry', "variable":'Industry'}, 
                  title=' Volatility Comparsion between ' + str(industry_merged.columns[0] + " & " + str(industry_merged.columns[1])
                  ))
    fig.update_layout(legend=dict(yanchor="bottom", y=0.90,xanchor="right", x=0.99 ),
                      title={
                        #'y':0.97,
                        #x':0.3,
                        'xanchor': 'auto',
                        'yanchor': 'auto'},
                      xaxis=dict(
                            rangeselector=dict(
                                buttons=list([
                                    dict(count=6,
                                         label="6m",
                                         step="month",
                                         stepmode="backward"),
                                    dict(count=1,
                                         label="1y",
                                         step="year",
                                         stepmode="backward"),
                                    dict(count=5,
                                         label="5y",
                                         step="year",
                                         stepmode="backward"),
                                    dict(count=10,
                                         label="10y",
                                         step="year",
                                         stepmode="backward"),
                                    dict(step="all")
                                ])
                            ),
                            rangeslider=dict(
                                visible=True
                            ),
                            type="date"
    )
                     )
    return fig


##For single volatility
def plot_volatility(df, start, end, industry):
    industry = industry_preprocess(df, start, end, industry)
    industry['Volatility'] = industry.pct_change() * 100
    industry.dropna(inplace=True)
    #fig = plot_industry(pd.DataFrame(industry['Volatility']))
    
    fig = px.line(
        industry,
        x=industry.index,
        y=industry.columns[1],
        title="Change by Volatility (in %)",
        labels = {'index':'Date',industry.columns[1]: 'Change %'}
    )
    fig.update_layout(height=500, width=725 , autosize=True,
            title={
            'xanchor': 'auto',
            'yanchor': 'auto'},
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(count=5,
                     label="5y",
                     step="year",
                     stepmode="backward"),
                dict(count=10,
                     label="10y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    ))
    return fig
    

def plot_models(df, industry_name):
    
    with ZipFile('models.zip') as zip:
        with zip.open('Total Employment.pkl') as myZip:
            result1 = pickle.load(myZip)
    zip.close()
    with ZipFile('model_covid.zip') as zip:
        with zip.open('Total Employment_covid.pkl') as myZip:
            result2 = pickle.load(myZip)
    zip.close()
    #model1 = 'models/'+str(industry_name)+'.pkl'
    #model2 = 'models_covid/'+str(industry_name)+'_covid.pkl'
    #result1 = pickle.load(open(model1, 'rb'))
    #result2 = pickle.load(open(model2, 'rb'))

    mean_forecast1, lower_limits1, upper_limits1 = forecast_results(result1, industry_name)
    mean_forecast2, lower_limits2, upper_limits2 = forecast_results(result2, industry_name)
    
    industry_total = industry_preprocess(df, 'January 1987', 'January 2021', industry_name)
    mean_forecast1, mean_forecast2 = pd.DataFrame(mean_forecast1), pd.DataFrame(mean_forecast2)
    lower_limits1, upper_limits1 = pd.DataFrame(lower_limits1), pd.DataFrame(upper_limits1)
    lower_limits2, upper_limits2 = pd.DataFrame(lower_limits2), pd.DataFrame(upper_limits2)
    
    actual = go.Scatter(x=industry_total.index, y=industry_total[industry_name],
                    name='Observed', mode='lines',line = dict(color = 'blue'))

    predict = go.Scatter(x=mean_forecast1.index, y=mean_forecast1['predicted_mean'],
                         name='Forecast without Covid-19', mode='lines', line= dict(color='green'))

    lower_limit1 = go.Scatter(x=lower_limits1.index, y=lower_limits1['lower '+str(industry_name)],
                              mode='none',fill = 'tonexty', fillcolor='rgba(157, 210, 183, 0.3)', showlegend=False)

    upper_limit1 = go.Scatter(x=upper_limits1.index, y=upper_limits1['upper '+str(industry_name)],
                              mode='none',fill = 'tonexty', fillcolor='rgba(157, 210, 183, 0.3)', showlegend=False)

    predict_covid = go.Scatter(x=mean_forecast2.index, y=mean_forecast2['predicted_mean'],
                         name='Forecast with Covid-19', mode='lines', line= dict(color='red'))

    lower_limit2 = go.Scatter(x=lower_limits2.index, y=lower_limits2['lower '+str(industry_name)],
                              mode='none',fill = 'tonexty', fillcolor='rgba(238, 154, 154, 0.3)', showlegend=False)

    upper_limit2 = go.Scatter(x=upper_limits2.index, y=upper_limits2['upper '+str(industry_name)],
                              mode='none',fill = 'tonexty', fillcolor='rgba(157, 154, 154, 0.3)', showlegend=False)



    layout = go.Layout(height=600, title="The Employment Forecasting for " + str(industry_name) + " With and Without Covid Pandemic",
                yaxis=dict(title='Value x1000'),
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01),
                xaxis=dict(title='Year',
                        rangeselector=dict(
                            buttons=list([
                                dict(count=6,
                                     label="6m",
                                     step="month",
                                     stepmode="backward"),
                                dict(count=1,
                                     label="1y",
                                     step="year",
                                     stepmode="backward"),
                                dict(count=5,
                                     label="5y",
                                     step="year",
                                     stepmode="backward"),
                                dict(count=10,
                                     label="10y",
                                     step="year",
                                     stepmode="backward"),
                                dict(step="all")
                                            ])),
                        rangeslider=dict(visible=True),
                type="date"))
    data_fig = [actual, predict, lower_limit1, upper_limit1, predict_covid, lower_limit2, upper_limit2]
    fig = go.Figure(data=data_fig, layout=layout)
    return fig

def forecast_results(results,industry_name):
    forecast = results.get_forecast(steps =72)
    mean_forecast= forecast.predicted_mean
    confidence_intervals= forecast.conf_int()
    confidence_intervals
    # Select lower and upper confidence limits
    lower_limits = confidence_intervals.loc[:,'lower '+ str(industry_name)]
    upper_limits = confidence_intervals.loc[:,'upper '+ str(industry_name)]

    # Print best estimate predictions
    #print(mean_forecast2)
    return mean_forecast, lower_limits, upper_limits

def plot_forecasted(industry_name):
    location_file = 'Forecasted/'+str(industry_name)+'.pkl'
    figure = pickle.load(open(location_file, 'rb'))
    return figure