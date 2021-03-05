import plotly.express as px
import plotly.offline as pyo

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
                 marginal_x="box", trendline="ols", template="simple_white")
pyo.plot(fig, filename='data/plotlyPlots/plotly5.html')
