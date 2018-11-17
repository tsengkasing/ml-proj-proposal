# -*-coding:utf-8-*-

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


def preprocess(feature_set):
    scaler = StandardScaler()
    scaler.fit(feature_set)
    return scaler


def train(feature_set, label_set):
    clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(100, 50))
    clf.fit(feature_set, label_set)
    return clf

