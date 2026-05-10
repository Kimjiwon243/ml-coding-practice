# -*- coding: utf-8 -*-
# 선형 SVM 분류

import numpy as np
import sklearn.datasets import load_iris
import sklearn.pipeline import make_pipeline
import sklearn.preprocessing import StandardScaler  
import sklearn.svm import SVC

iris = load_iris(as_frame=True)
X = iris.data[["petal length (cm)", "petal width (cm)"]].values
y = (iris.target == 2)  # Iris virginica

svm