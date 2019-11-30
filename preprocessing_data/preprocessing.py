import numpy as np
import matplotlib.pyplot as plt
from preprocessing_data.get_data import *


def information_dataset(data):
    classe_1 = data['sepal_length'].loc[data['species'] == "virginica"]
    classe_2 = data['sepal_length'].loc[data['species'] == "virginica"]
    print("Forme du jeu de données adult_data.csv : ", data.shape)
    print("nombre de personnes dans la classe 1", classe_1.shape )
    print("nombre de personnes dans la classe 2", classe_2.shape)
    print(data.sample(frac=0.7).head())
    return

if __name__ == '__main__':
    information_dataset(data_train)
