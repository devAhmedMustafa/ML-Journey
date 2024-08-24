from StarAI.Plotting.Plot import *
from StarAI.Models.LinearRegression import LinearRegression
from StarAI.Models.LogisticRegression import LogisticRegression


def plot_linear_model(lm: LinearRegression):
    idx = 0
    for f in lm.x:
        plot_points(lm.x[f], lm.y, lm.x[f].name, lm.y.name)
        plot_linear(lm.weights[idx], lm.bias, lm.x[f])

        idx += 1

        show()


def plot_logistic_model(lm: LogisticRegression):
    idx = 0
    for f in lm.x:
        plot_points(lm.x[f], lm.y, lm.x[f].name, lm.y.name)
        plot_sigmoid(lm.weights[idx], lm.bias, lm.x[f])
        idx += 1

        show()

