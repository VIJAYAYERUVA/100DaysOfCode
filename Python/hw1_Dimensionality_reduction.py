# imports
import numpy.linalg as linalg

import numpy as np

# Read the data from https://archive.ics.uci.edu/ml/datasets/Cloud
data = np.loadtxt('data/input/cloud.data')


# function to center the data
def center(data):
    data_mean = np.mean(data, axis=0)
    centered_data = data - data_mean
    return centered_data


centered_data = center(data)


# function to compute the covariance of the centered the data
def covar(centered_data):
    num_rows, num_cols = centered_data.shape
    covariance_matrix = (1 / num_rows) * np.matmul(centered_data.T, centered_data)
    return covariance_matrix


covariance_matrix = covar(centered_data)

# Compute the eigenvectors and eigenvalues
W, Vec = linalg.eig(covariance_matrix)


# function to find the number of principal components (PCs)
def reducedr(eigval, alpha):
    # print(eigvec.shape)
    totalsum = 0
    for i in range(len(eigval)):
        totalsum += eigval[i]
    # print(totalsum)

    partialsum = 0
    retainedcomponents = []
    count = 0

    for i in range(len(eigval)):
        partialsum += eigval[i]
        frac = partialsum / totalsum
        # print(frac)
        retainedcomponents.append(eigval[i])
        count = count + 1

        if frac >= alpha:
            break
            # return(count,retainedcomponents)
    return count, retainedcomponents


# calculating number of PCs
PCs = reducedr(W, 0.9)


# function to get first two components
def getxy(data):
    x = []
    y = []

    for i in range(1024):
        x.append(1)
        y.append(data[i, 0])
    for i in range(1024):
        x.append(2)
        y.append(data[i, 1])

    return x, y


x, y = getxy(data)

c1 = data[:, 0]
c2 = data[:, 1]
# write first two components to text file
np.savetxt('data/output/Components.txt', X=(c1, c2), delimiter=',')

import plotly.express as px
import plotly.offline as pyo

fig = px.scatter(
    x=x,
    y=y,
    labels={"x": 'Components',
            "y": 'Magnitude'})

fig.update_layout(font=dict(family="Times New Roman",
                            size=18,
                            color="blue"),
                  title={'text': 'First two components in the given data',
                         'x': 0.5,
                         'xanchor': 'center'
                         },
                  xaxis=dict(tickmode='array',
                             tickvals=[1, 2],
                             ticktext=['component1', 'component2']),
                  margin=dict(l=0, r=0, b=0)
                  )

fig.show()
pyo.plot(fig, filename='data/output/plotlyPlots/First_two_components.html', auto_open=False)

u1 = Vec[0]
u2 = Vec[1]

a1 = np.matmul(data, u1)
a2 = np.matmul(data, u2)

fig = px.scatter(
    x=a1,
    y=a2,
    labels={"x": 'a1',
            "y": 'a2'})

fig.update_layout(font=dict(family="Times New Roman",
                            size=18,
                            color="blue"),
                  title={'text': 'Projected data on first two PCs',
                         'x': 0.5,
                         'xanchor': 'center'
                         },
                  margin=dict(l=0, r=0, b=0)
                  )

fig.show()
pyo.plot(fig, filename='data/output/plotlyPlots/Reduced_dimension.html', auto_open=False)

from sklearn.decomposition import PCA

pca = PCA(n_components=10)
pca.fit(data)

# get and print the covariance matrix from sklearn' PCA
# print(pca.get_covariance(), '\n')

# get and print the covariance matrix from sklearn' PCA
print(pca.explained_variance_)

# End of file
