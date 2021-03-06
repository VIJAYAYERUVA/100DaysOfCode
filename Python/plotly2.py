import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Set poll data as pandas DataFrame
data = pd.read_csv('data/All_D_topics.csv')

EssayName = 'Agamemnon'
df = data.loc[data['EssayName'] == EssayName]
df.reset_index(drop=True, inplace=True)

x_values = df.ParagraphNumber
y_values = df.compound

# create traces
trace1 = go.Scatter(
    x=x_values,
    y=y_values,
    mode='lines+markers',
    name='lines+markers'
)
data = [trace1]  # assign traces to data
layout = go.Layout(
    title='Line chart showing three different modes'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='data/plotlyPlots/plotly2.html')
