import plotly.express as px
import plotly.offline as pyo

df = px.data.tips()

fig = px.box(df, x="day", y="total_bill", color="smoker")
fig.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
pyo.plot(fig, filename='data/output/plotlyPlots/plotly10.html')
