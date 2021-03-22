import plotly.express as px
import plotly.offline as pyo

df = px.data.stocks(indexed=True)
fig = px.line(df)
fig.add_hline(y=1, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline",
              annotation_position="bottom right")
fig.add_vrect(x0="2018-09-24", x1="2018-12-18",
              annotation_text="decline", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
pyo.plot(fig, validate=False, filename='data/output/plotlyPlots/plotly21.html')
