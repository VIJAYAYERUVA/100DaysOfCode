import plotly.express as px
import plotly.offline as pyo

df = px.data.tips()

fig = px.density_contour(df, x="total_bill", y="tip")
fig.update_traces(contours_coloring="fill", contours_showlabels=True)
pyo.plot(fig, filename='data/plotlyPlots/plotly16.html')
