import plotly.express as px
import plotly.offline as pyo

df = px.data.tips()
fig = px.pie(df, values='tip', names='day', color_discrete_sequence=px.colors.sequential.RdBu)
pyo.plot(fig, filename='data/output/plotlyPlots/plotly9.html')
