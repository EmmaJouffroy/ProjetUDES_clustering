import os
import pandas as pd

data_dir = os.path.join('..', 'data', 'csv')
print(data_dir)

data_train = pd.read_csv(data_dir+"adult_data.csv", sep=',', na_values='␣', encoding='latin-1')
data_test = pd.read_csv(data_dir+"adult_test.csv", sep=',', na_values='␣', encoding='latin-1')