import pandas as pd
from StarAI.Models.LinearRegression import LinearRegression
from StarAI.Workflow.Data import *
from StarAI.Plotting.Models import *
from Workflow.Analysis import *


if __name__ == "__main__":

    x_train, x_test, y_train, y_test = clean_data("./Datasets/Book1.csv", 'Watching Time', ['ID', 'Name', 'Gender'])

    model = LinearRegression()
    model.fit(x_train, y_train)
    plot_logistic_model(model)

    y_pred = model.predict(x_test)

    print(mean_square_error(y_test, y_pred))

    # x_train, x_test, y_train, y_test = clean_data("./Datasets/Book1.csv", 'Watching Time', ['ID', 'Name', 'Gender'])
    #
    # lm = LinearRegression()
    # lm.fit(x_train, y_train)
    # plot_linear_model(lm)
    #
    # y_predict = lm.predict(x_test)
    #
    # print(mean_square_error(y_predict, y_test))


