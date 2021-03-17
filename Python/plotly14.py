import plotly.express as px
import plotly.offline as pyo

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]
fig = px.scatter_matrix(df, dimensions=features, color="species")
pyo.plot(fig, filename='data/output/plotlyPlots/plotly14.html')
