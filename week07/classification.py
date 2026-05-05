# -*- coding: utf-8 -*-
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', as_frame=False)

print(mnist.keys())  # data와 target만 사용

X, y = mnist.data, mnist.target
print(X)
print(X.shape)       # 28 x 28 개의 픽셀 특징을 가진 이미지 70,000개
print(y)
print(y.shape)

import matplotlib.pyplot as ply

def plot_digit(data):
    image = data.reshape(28, 28)
    ply.imshow(image, cmap=ply.cm.binary, interpolation='nearest')
    ply.axis('off')

some_digit = X[0]
plot_digit(some_digit)
ply.show()

print(y[0])         # 샘플 데이터 레이블 확인 (=5)

# 10x10 그림 생성

