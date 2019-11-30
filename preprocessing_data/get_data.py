import os
import pandas as pd

# data_dir = os.path.join('SDD', 'data', 'csv')

# data_train = pd.read_csv(data_dir+"/adult_data.csv", sep=',', na_values='␣', encoding='latin-1')
# data_test = pd.read_csv(data_dir+"/adult_test.csv", sep=',', na_values='␣', encoding='latin-1')

data_train = pd.read_csv("../data/csv/adult_data.csv", sep=',', na_values='␣', encoding='latin-1')
data_test = pd.read_csv("../data/csv/adult_test.csv", sep=',', na_values='␣', encoding='latin-1')