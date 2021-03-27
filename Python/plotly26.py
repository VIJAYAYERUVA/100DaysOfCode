import plotly.graph_objects as go
import plotly.offline as pyo

years = ['2016', '2017', '2018']

fig = go.Figure()
fig.add_trace(go.Bar(x=years, y=[500, 600, 700],
                     base=[-500, -600, -700],
                     marker_color='crimson',
                     name='expenses'))
fig.add_trace(go.Bar(x=years, y=[300, 400, 700],
                     base=0,
                     marker_color='lightslategrey',
                     name='revenue'
                     ))

pyo.plot(fig, validate=False, filename='data/output/plotlyPlots/plotly26.html')
