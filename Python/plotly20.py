import plotly.express as px
import plotly.offline as pyo

df = px.data.iris()
fig = px.scatter(df, x="petal_length", y="petal_width")
fig.add_vline(x=2.5, line_width=3, line_dash="dash", line_color="green")
fig.add_hrect(y0=0.9, y1=2.6, line_width=0, fillcolor="red", opacity=0.2)
pyo.plot(fig, validate=False, filename='data/output/plotlyPlots/plotly20.html')
