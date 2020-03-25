import pyforest
import plotly
import chart_studio
import chart_studio.plotly as py
import cufflinks as cf
import chart_studio.tools as tls
import plotly.graph_objs as go
from plotly.subplots import make_subplots
chart_studio.tools.set_credentials_file(username='user_name', api_key='xxxxxxxxxxxxxxxxxx')
from pandas.io.formats.style import Styler
import plotly.express as px


df = pd.read_csv('Covid-19-dataset/24_03_2020_Italia_Covid-19.csv')
df.index +=1
df['Total New Cases'] = df['Total New Cases'].apply(int)
df.style.format({
    'Total Cases': '{:,}'.format,
    'Total New Cases': '{:,}'.format
})

fig = make_subplots(specs=[[{"secondary_y": True}]]) #this a one cell subplot
trace1 = go.Bar(
                    x=df.Date,
                    y=df['Total New Cases'],
                    name="Total Daily New Cases",
                    marker_color = 'rgb(0, 128, 255)'
                    #marker=dict(color= 'blue') 
                    #        line= dict(width= 1))
)
 
trace2 = go.Scatter(
                    x=df.Date,
                    y=df['% Daily Increase in Cases'],
                    name="% Daily Increase in Cases",
                    mode='lines+markers',
                    marker_color = 'rgb(255, 83, 26)'
                    
                    )

fig.add_trace(trace1, secondary_y=False);
fig.add_trace(trace2, secondary_y=True);


fig.update_layout(autosize= True, 
                  width= 1050, 
                  height= 600, 
                  legend=dict(x=0, y=1.2),
                  yaxis = dict(linecolor='rgb(400, 400, 900)',
        linewidth=2,),
                  hovermode='x'
                  );
fig.update_xaxes(tickangle= -45, 
                 autorange=True,
                 tickfont=dict(size= 10), 
                );

fig.update_yaxes(range= [0, 8000], #left yaxis
                 title= 'Daily New Cases', secondary_y=False, 
                 tickfont=dict(color='rgb(0, 128, 255)'),
                title_font=dict(size=14, color='rgb(0, 128, 255)'));

fig.update_yaxes(range= [0, 100], #right yaxis
                 showgrid= False, 
                 title= '% Daily Increase',
                 linecolor='rgb(255, 83, 26)',
                 tickfont=dict(color='rgb(255, 83, 26)'),
                 title_font=dict(size=14, color='red'),
                 secondary_y=True);
fig.show()

