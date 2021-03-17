import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Set poll data as pandas DataFrame
df = pd.read_csv('data/2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY      '] == day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)
layout = go.Layout(title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
                   hovermode='closest')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='data/output/plotlyPlots/plotly6.html')
