import plotly.express as px
import plotly.offline as pyo

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]

fig = px.scatter_matrix(
    df,
    dimensions=features,
    color="species"
)
fig.update_traces(diagonal_visible=False)
pyo.plot(fig, filename='data/output/plotlyPlots/Reduced_dimensions.html')
