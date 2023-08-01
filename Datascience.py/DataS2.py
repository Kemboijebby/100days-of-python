import openpyxl
#pandas library is used in handling tabular data
import pandas as pd
launch_data = pd.read_excel("RocketLaunchDataCompleted.xlsx")
#print(launch_data.info())
def data_manipulation(launch_data):
    launch_data.info()
    launch_data['Launched?'].fillna('N',inplace=True)
    launch_data['Crewed or Uncrewed'].fillna('Uncrewed',inplace=True)
    launch_data['Wind Direction'].fillna('unknown', inplace=True)
    launch_data['Condition'].fillna('Fair',inplace=True)
    launch_data.fillna(0,inplace=True)
    launch_data.head()
    print(launch_data.info())

    #launch_data.columns
data_manipulation(launch_data)


#Numpy is used for handling numerical series operations(addition,multiplication,..)
import numpy as np
import matplotlib.pyplot as plt
#Sklearn library contains all machine learning packages we need to digest and exract patterns from data
from sklearn.datasets import load_iris
# iris= load_iris()
# df=pd.DataFrame(data=iris["data"],columns=iris["feature_names"])
# print(df.head())
from sklearn import linear_model,model_selection,metrics
from sklearn.model_selection import train_test_split


#machine learning libraries used to build a decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

launch_data2=data_manipulation(launch_data)
#sklearn's preprocessing library is used for processing and cleaning the data
from  sklearn import preprocessing
## As part of the data cleaning process, we have to convert text data to numerical because computers understand only numbers
def data_man2(launch_data2):
    label_encoder = preprocessing.LabelEncoder()

    # Three columns have categorical text info, and we convert them to numbers
    launch_data['Crewed or Uncrewed'] = label_encoder.fit_transform(launch_data['Crewed or Uncrewed'])
    launch_data['Wind Direction'] = label_encoder.fit_transform(launch_data['Wind Direction'])
    launch_data['Condition'] = label_encoder.fit_transform(launch_data['Condition'])
    print(launch_data2.head())
data_man2(launch_data)

#for visualizing the tree
import pydotplus
from IPython.display import Image