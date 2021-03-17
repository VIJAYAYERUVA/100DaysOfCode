import plotly.express as px
import plotly.offline as pyo
from sklearn.manifold import TSNE

df = px.data.iris()

features = df.loc[:, :'petal_width']

tsne = TSNE(n_components=3, random_state=0)
projections = tsne.fit_transform(features, )

fig = px.scatter_3d(
    projections, x=0, y=1, z=2,
    color=df.species, labels={'color': 'species'}
)
fig.update_traces(marker_size=8)
pyo.plot(fig, filename='data/output/plotlyPlots/plotly15.html')
