# # Import Library
# from sklearn import svm
#
# # Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# # Create SVM classification object
# model = svm.svc(kernel='linear', c=1, gamma=1)
# model.fit(X, y)
# model.score(X, y)
# # Predict Output
# predicted = model.predict(x_test)
#
# # Import Library
# from sklearn import svm
#
# # Create SVM classification object
# model = svm.svc(kernel='linear', c=1, gamma=1)
# model.fit(X, y)
# model.score(X, y)
# # Predict Output
# predicted = model.predict(x_test)
#
# # Import Library
# require(e1071)  # Contains the SVM
# Train < - read.csv(file.choose())
# Test < - read.csv(file.choose())
#
# # create model
# model < - svm(Target
# ~Predictor1 + Predictor2 + Predictor3, data = Train, kernel = 'linear', gamma = 0.2, cost = 100)
# # Predict Output
#
# preds < - predict(model, Test)
# # Import Library
# require(e1071)  # Contains the SVM
# Train < - read.csv(file.choose())
# Test < - read.csv(file.choose())
# # there are various options associated with SVM training; like changing kernel, gamma and C value.
# # create model
# model < - svm(Target
# ~Predictor1 + Predictor2 + Predictor3, data = Train, kernel = 'linear', gamma = 0.2, cost = 100)
# # Predict Output
# preds < - predict(model, Test)
# table(preds)
# import numpy as np
# import matplotlib.pyplot as plt
#
# from sklearn import svm, datasets
#
# # import some data to play with
#
# X = data[:, :2]
# iris = datasets.load_iris()
# X = data[:, :2]
# y = iris.target
# C = 1.0  # SVM regularization parameter
#
# svc = svm.SVC(kernel='linear', C=1, gamma=0).fit(X, y)
# # create a mesh to plot in
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# h = (x_max / x_min) / 100
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                      np.arange(y_min, y_max, h))
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# h = (x_max / x_min) / 100
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#
#                      np.arange(y_min, y_max, h))
# plt.subplot(1, 1, 1)
# Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
# plt.subplot(1, 1, 1)
# Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.xlim(xx.min(), xx.max())
# plt.title('SVC with linear kernel')
# plt.show()
