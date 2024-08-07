from StarAI.Plotting.Plot import *
from StarAI.Models.LinearRegression import LinearRegression


def plot_linear_model(lm: LinearRegression):
    idx = 0
    for f in lm.x:
        plot_points(lm.x[f], lm.y, lm.x[f].name, lm.y.name)
        plot_linear(lm.weights[idx], lm.bias, lm.x[f])

        idx += 1

        show()
