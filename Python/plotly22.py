import plotly.express as px
import plotly.offline as pyo

df = px.data.gapminder()

fig = px.bar(df, x="continent", y="pop", color="continent",
             animation_frame="year", animation_group="country", range_y=[0, 4000000000])
pyo.plot(fig, validate=False, filename='data/output/plotlyPlots/plotly22.html')
