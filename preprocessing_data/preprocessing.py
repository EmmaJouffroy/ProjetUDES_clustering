import numpy as np
import matplotlib.pyplot as plt
from preprocessing_data.get_data import *


def information_dataset(data):
    data.sample(frac=0.7).head()
    return

if __name__ == '__main__':
    information_dataset(data_train)