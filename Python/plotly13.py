import plotly.graph_objects as go
import plotly.offline as pyo

fig = go.Figure(data=go.Heatmap(
    z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    y=['Morning', 'Afternoon', 'Evening'],
    hoverongaps=False))
pyo.plot(fig, filename='data/plotlyPlots/plotly13.html')
