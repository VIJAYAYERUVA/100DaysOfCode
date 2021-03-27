import plotly.express as px
import plotly.offline as pyo

data = [[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
fig = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                y=['Morning', 'Afternoon', 'Evening']
                )
fig.update_xaxes(side="top")
pyo.plot(fig, validate=False, filename='data/output/plotlyPlots/plotly24.html')
