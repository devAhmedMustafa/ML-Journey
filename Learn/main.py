import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from LinearRegressionModel import LinearRegression

from KMeansClustering import KMeans
from LogisticRegressionModel import LogisticRegression

df = pd.read_csv("train.csv")
print(df.head())
df = df[["LotArea", "SalePrice"]]
df.rename(columns={"BedroomAbvGr": "Bedrooms"}, inplace=True)

df = df.dropna()

X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=121)

# fig = plt.figure(figsize=(8, 6))

# lm = LinearRegression(lr=0.01)
# lm.fit(X_train, y_train)
# pred = lm.predict(X_test)

# def mse(y_test, predictions):
#     return np.mean((y_test-predictions)**2)

# error = mse(y_test, pred)
# print(error)


# if __name__ == "__main__":
#     np.random.seed(42)
#     from sklearn.datasets import make_blobs
#
#     X, y = make_blobs(
#         centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40
#     )
#     print(X.shape)
#
#     clusters = len(np.unique(y))
#     print(clusters)
#
#     k = KMeans(K=clusters, max_iters=1, plot_steps=True)
#     y_pred = k.predict(X)
#
#     k.plot()
