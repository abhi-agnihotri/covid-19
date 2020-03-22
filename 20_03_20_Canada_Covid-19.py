# Importing libraries

import pyforest
import plotly
import chart_studio
import chart_studio.plotly as py
import cufflinks as cf
import chart_studio.tools as tls
import plotly.graph_objs as go
chart_studio.tools.set_credentials_file(username='Plotly_user_name', api_key='##########')
from pandas.io.formats.style import Styler
import plotly.express as px

# Importing data into a dataframe
df = pd.read_excel('Filename.xls')
df.index +=1

# Basic data cleaning
df.style.format({'BC % Increase': "{:.2%}", 'AB % Increase': "{:.2%}", 'QC % Increase': "{:.2%}", 'ON % Increase': "{:.2%}"})
df[['BC % Increase', 'AB % Increase', 'QC % Increase', 'ON % Increase']] = df[['BC % Increase', 'AB % Increase', 'QC % Increase', 'ON % Increase']]*100
df[['BC % Increase', 'AB % Increase', 'QC % Increase', 'ON % Increase']] = df[['BC % Increase', 'AB % Increase', 'QC % Increase', 'ON % Increase']].round(2)
df

# Plotly function to plot increase in cases by Province with Time
fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df.Date,
                y=df['BC # Increase'],
                name="BC",
))

fig.add_trace(go.Scatter(
                
                x=df.Date,
                y=df['AB # Increase'],
                name="AB",
))

fig.add_trace(go.Scatter(
                
                x=df.Date,
                y=df['QC # Increase'],
                name="QC",
))

fig.add_trace(go.Scatter(
            
                x=df.Date,
                y=df['ON # Increase'],
                name="ON",
                line_color='black',
))

fig.update_layout(
    title="COVID-19 Cases By Province",
    xaxis_title="Date",
    yaxis_title="Total Cases",
    #font=dict(
    #    family="Courier New, monospace",
    #    size=10,
    #    color="#7f7f7f"
    
)

fig.show()

# Plotly function to plot Percentage Daily Increase by Province with time
fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df.Date,
                y=df['BC % Increase'],
                name="BC",
                opacity=0.4
))

fig.add_trace(go.Scatter(
                
                x=df.Date,
                y=df['AB % Increase'],
                name="AB",
                opacity=0.4
))

fig.add_trace(go.Scatter(
                
                x=df.Date,
                y=df['QC % Increase'],
                name="QC",
                #line_color='dimgray',
                opacity=0.4
))

fig.add_trace(go.Scatter(
            
                x=df.Date,
                y=df['ON % Increase'],
                name="ON",
                line_color='black',
                #opacity=0.1
))

fig.update_layout(
    title="COVID-19 Percentage Change By Province",
    xaxis_title="Timeline",
    yaxis_title="% Increase from Previous Day",
    #font=dict(
    #    family="Courier New, monospace",
    #    size=10,
    #    color="#7f7f7f"
    
)
fig.show()



