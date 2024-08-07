import numpy as np


def mean_square_error(y, y_pred):
    return np.mean(np.power(y-y_pred, 2))