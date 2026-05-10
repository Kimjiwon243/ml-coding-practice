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

svm_clf = make_pipeline(StandardScaler(),
                        LinearSVC(C=1, dual=True, random_state=42))
svm_clf.fit(X, y)
X_new = [[5.5, 1.7], [5.0, 1.5]]

print(svm_clf.predict(X_new))
print(svm_clf.decision_function(X_new))

