import pandas as pd
import plotly.io as pio
import plotly.offline as pyo

df = pd.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/worldhappiness.csv")

aggs = ["count", "sum", "avg", "median", "mode", "rms", "stddev", "min", "max", "first", "last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)

data = [dict(
    type='choropleth',
    locationmode='country names',
    locations=df['Country'],
    z=df['HappinessScore'],
    autocolorscale=False,
    colorscale='Portland',
    reversescale=True,
    transforms=[dict(
        type='aggregate',
        groups=df['Country'],
        aggregations=[dict(
            target='z', func='sum', enabled=True)
        ]
    )]
)]

layout = dict(
    title='<b>Plotly Aggregations</b><br>use dropdown to change aggregation',
    xaxis=dict(title='Subject'),
    yaxis=dict(title='Score', range=[0, 22]),
    height=600,
    width=900,
    updatemenus=[dict(
        x=0.85,
        y=1.15,
        xref='paper',
        yref='paper',
        yanchor='top',
        active=1,
        showactive=False,
        buttons=agg_func
    )]
)

fig_dict = dict(data=data, layout=layout)
pio.show(fig_dict, validate=False)
pyo.plot(fig_dict, validate=False, filename='data/output/plotlyPlots/plotly17.html')
