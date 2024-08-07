import numpy as np
from StarAI.Math.Math import *


class LogisticRegression:

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

        for _ in range(self.n_iters):
            linear_f = np.dot(x, self.weights) + self.bias
            sigmoid_f = sigmoid(linear_f)

            dw = np.dot(x.T, sigmoid_f-y)/n_samples
            db = np.sum(sigmoid_f-y)/n_samples

            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    def predict(self, x):
        linear_pred = np.dot(x, self.weights) + self.bias
        y_pred = sigmoid(linear_pred)
        class_pred = [0 if y <= 0.5 else 1 for y in y_pred]
        return class_pred
