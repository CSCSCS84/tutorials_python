# Exercise for Udemy course: python-for-data-science-and-machine-learning-bootcamp/
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

customers = pd.read_csv("data/customers.csv")


def linear_Regression():
    global X, y_test, lm, y_pred
    X = customers[["Avg. Session Length", "Time on App", "Time on Website", "Length of Membership"]]
    y = customers["Yearly Amount Spent"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    y_pred = pd.Series(lm.predict(X_test))


def analysis_before_prediction():
    print(customers.head())
    print(customers.info())
    print(customers.describe())
    print(customers.columns)
    sns.jointplot(x="Time on Website", y="Yearly Amount Spent", data=customers)
    sns.jointplot(x="Time on App", y="Yearly Amount Spent", data=customers)
    sns.jointplot(x="Time on App", y="Length of Membership", data=customers, kind="hex")
    sns.pairplot(data=customers)

    sns.lmplot(x="Length of Membership", y="Yearly Amount Spent", data=customers)

    sns.pairplot(customers)
    sns.distplot(customers["Yearly Amount Spent"])
    sns.heatmap(customers.corr(), cmap="coolwarm")


def analysis_after_prediction():
    coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
    plt.scatter(y_test.values, y_pred.values)
    plt.xlabel('Y Test')
    plt.ylabel('Predicted Y')
    # plot the residuals
    sns.displot((y_test - y_pred), bins=50)
    print(coeff_df)
    print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
    print('MSE:', metrics.mean_squared_error(y_test, y_pred))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# analysis_before_prediction()
linear_Regression()
analysis_after_prediction()
plt.show()
