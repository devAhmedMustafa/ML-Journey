import numpy as np


def upper_feature(col):

    new_col = np.array(col)
    for i in range(len(col)):
        new_col[i] = col[i].upper()

    return new_col
