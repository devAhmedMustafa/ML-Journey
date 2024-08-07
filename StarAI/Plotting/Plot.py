import matplotlib.pyplot as plt
import numpy as np


def plot_points(x, y, x_label="x-axis", y_label="y-axis", title="Plot dataset"):

    plt.scatter(x, y, color="green", marker='*')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    # plt.legend()


def plot_linear(m, c, X):

    x = np.linspace(np.min(X), np.max(X), 100)
    y = x*m + c

    plt.plot(x, y)

def show():
    plt.show()

if __name__ == "__main__":

    x = np.array([1,2,3,4,5])
    y = np.array([1,2,3,4,5])

    plot_points(x, y)
    plot_linear(10, 1, x)
    show()