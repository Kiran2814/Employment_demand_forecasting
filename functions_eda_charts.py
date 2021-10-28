

# In[234]:
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import plotly.express as px
# In[238]:


def plot_gender(data, industry_name):
    df = data[(data.NOC==industry_name)]
    df = df[(df.GEO =='Canada') & (df.Labour_characteristics == 'Labour force')]
    df = df[df['Sex'] != 'Both sexes'].fillna(0)
    fig = px.pie(df, values = 'VALUE', names = 'Sex', color='Sex', color_discrete_map={'Males': 'blue', 'Females':'magenta'})
    fig.update_layout(
        autosize=True,
        width=400,
        height=450,
        title={
            'text': 'Gender Distribution',
            'y':0.9,
            'x':0.45,
            'xanchor': 'center',
            'yanchor': 'top'})
    return fig



# In[240]:


def plot_labour(data, industry_name):
    df1 = data[data['NOC'] == industry_name]
    df1 = df1[(df1.GEO == 'Canada') & (df1.Sex == 'Both sexes')].fillna(0)

    fig=px.bar(df1, x=df1['Labour_characteristics'], y=df1['VALUE'],
               color=df1['Labour_characteristics'], labels = {'VALUE':'VALUE x1000'})
    fig.update_layout(
            autosize=True,
            showlegend=False,
            width=470,  
            height=400,
            title={
                'text': 'Employment Types',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'bottom'})
    return fig



# In[307]:


def plot_map(data, industry_name):
    geo_data = data[(data.NOC == industry_name)]
    geo_data = geo_data[(geo_data.GEO != 'Canada') & (geo_data.Labour_characteristics == 'Labour force')]
    geo_data = geo_data[(geo_data.Sex == 'Both sexes')].fillna(0)
    fig = px.scatter_geo(geo_data, lat='lat', lon='long', size='VALUE', color='GEO', size_max=65)
    fig.update_geos(
        lataxis = dict(range=[45,70]),
        lonaxis = dict(range=[-140,-60]),
        visible=False, resolution=50, scope="north america",
        framecolor='white',
        showland=True,
        landcolor='#dfe9ed',
        showocean=True,
        oceancolor='white',
        showsubunits=True, subunitcolor='black')
    fig.update_layout(plot_bgcolor='black',showlegend=False, height=500, width=1200,
                  title={
                        'text': 'Geographical Concentration of Jobs',
                        'y':0.97,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'})
    return fig
