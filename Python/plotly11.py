import plotly.figure_factory as ff
import plotly.offline as pyo

import numpy as np

x1, y1 = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u1 = np.cos(x1) * y1
v1 = np.sin(x1) * y1

fig = ff.create_quiver(x1, y1, u1, v1)

pyo.plot(fig, filename='data/plotlyPlots/plotly11.html')
