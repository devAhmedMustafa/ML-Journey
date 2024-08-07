import numpy as np


class LinearRegression:

    def __init__(self, lr=0.001, n_iters=100):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.x = None
        self.y = None

    def fit(self, x, y):

        self.x = x
        self.y = y

        n_samples, n_features = x.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):

            f = np.dot(x, self.weights) + self.bias
            dw = (np.dot(x.T, (f - y))) / n_samples
            db = (np.sum(f - y))/n_samples

            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    def predict(self, x):
        return np.dot(x, self.weights) + self.bias
