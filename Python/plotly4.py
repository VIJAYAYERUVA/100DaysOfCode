#######
# This line chart shows U.S. Census Bureau
# population data from six New England states.
# THIS PLOT USES PANDAS TO EXTRACT DESIRED DATA FROM THE SOURCE
######
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv(
    'https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')

# grab just the six New England states:
df2 = df[df['DIVISION'] == '1']

# set the index to state name:
df2.set_index('NAME', inplace=True)

# grab just the population columns:
df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode='markers+lines',
                   name=name) for name in df2.index]
pyo.plot(data, filename='data/output/plotlyPlots/plotly4.html')
