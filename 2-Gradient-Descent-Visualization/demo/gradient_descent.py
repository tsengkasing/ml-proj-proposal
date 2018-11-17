# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd


def compute_cost(X, y, theta):
    m = len(X)
    summands = 0.
    for i in range(m):
        hxi = 0.
        for j in range(len(X[i])):
            hxi += X[i][j] * theta[j][0]
        summands += (hxi - y[i][0]) ** 2
    cost = summands / (2 * m)
    return cost


def derivative(X, y, theta, j):
    m = len(X)
    step = 0.
    for _i in range(m):
        hx = 0.
        for _j in range(len(X[_i])):
            hx += X[_i][_j] * theta[_j][0]
        step += (hx - y[_i][0]) * X[_i][j] / m
    return step


async def gradient_descent(X, y, learning_rate, num_iterations, func):
    num_parameters = X.shape[1]
    theta = np.array([[0.0 for i in range(num_parameters)]]).T
    cost_list = [0.0 for i in range(num_iterations)]

    for it in range(num_iterations):
        theta_gradient = np.array([[derivative(X, y, theta, j) for j in range(num_parameters)]]).T
        theta -= learning_rate * theta_gradient
        cost_list[it] = compute_cost(X, y, theta)

        s = "Iteration {}: {}".format(str(it+1), cost_list[it])
        # if (it+1) % 100 == 0:
        await func(it+1, theta, theta_gradient, cost_list[it])
        # print(s)

    return theta, cost_list


async def run(func, num_iter = 100, alpha = 0.01):
    X_train, y_train, label = load_dataset(os.getcwd() + '/boston_train.csv')
    theta, cost_train = await gradient_descent(X_train, y_train, alpha, num_iter, func)


def load_dataset(train_path):
    train_data = pd.read_csv(train_path, sep=',').values
    label = pd.read_csv(train_path, sep=',').columns

    # m_train and m_test denote the number of training data and testing data
    m_train = train_data.shape[0]

    s_train_array = scaleFeature(train_data)

    train_append_ones = np.ones([m_train, 1])
    train_boston_hp_data = np.column_stack((train_append_ones, s_train_array))

    # train_columns and test_columns denote the number of columns of the modified training data and testing data
    train_columns = train_boston_hp_data.shape[1]

    X_train = train_boston_hp_data[:, 0:train_columns - 1]
    y_train = train_boston_hp_data[:, train_columns - 1:]

    return X_train, y_train, label


def scaleFeature(train_array):
    m_train = len(train_array)

    # array_mean stores the means of the training data
    array_mean = np.reshape(np.mean(train_array, axis=0), (1, -1))
    # array_range is difference between max and min values
    array_range = np.reshape(np.max(train_array, axis=0), (1, -1)) - np.reshape(np.min(train_array, axis=0), (1, -1))
    s_train_array = np.true_divide((train_array - np.repeat(array_mean, m_train, axis=0)), np.repeat(array_range, m_train, axis=0))
    return s_train_array


