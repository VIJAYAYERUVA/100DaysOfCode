# https://plotly.com/python/t-sne-and-umap-projections/

import plotly.express as px
import plotly.offline as pyo
from sklearn.manifold import TSNE

df = px.data.iris()

features = df.loc[:, :'petal_width']

tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(features)

fig = px.scatter(
    projections, x=0, y=1,
    color=df.species, labels={'color': 'species'}
)
pyo.plot(fig, filename='data/plotlyPlots/plotly3.html')
