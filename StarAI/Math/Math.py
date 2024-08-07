import numpy as np


def standard_deviation(sample):
    mean = np.mean(sample)

    return np.sum(np.power(sample-mean, 2))/sample.shape[0]


def sigmoid(x):
    return 1 / (1+np.exp(-x))


if __name__ == "__main__":
    sd = standard_deviation(np.array([1, 2, 3, 4, 0]))

    print(sd)
