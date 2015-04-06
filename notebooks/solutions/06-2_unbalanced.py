from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

for Class in [KNeighborsClassifier, GaussianNB, SVC]:
    cls = Class().fit(X_train, y_train)
    y_pred = cls.predict(X_test)
    print("-------------------------------------------")
    print(Class.__name__)
    print(metrics.classification_report(y_pred, y_test))