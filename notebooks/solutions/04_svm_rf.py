# SVM results
from sklearn.svm import SVC
from sklearn import metrics

for kernel in ['rbf', 'linear']:
    clf = SVC(kernel=kernel).fit(Xtrain, ytrain)
    ypred = clf.predict(Xtest)
    print("SVC: kernel = {0}".format(kernel))
    print(metrics.f1_score(ytest, ypred))
    plt.figure()
    plt.imshow(metrics.confusion_matrix(ypred, ytest),
               interpolation='nearest', cmap=plt.cm.binary)
    plt.colorbar()
    plt.xlabel("true label")
    plt.ylabel("predicted label")
    plt.title("SVC: kernel = {0}".format(kernel))
    
# random forest results
from sklearn.ensemble import RandomForestClassifier

for max_depth in [3, 5, 10]:
    clf = RandomForestClassifier(max_depth=max_depth).fit(Xtrain, ytrain)
    ypred = clf.predict(Xtest)
    print("RF: max_depth = {0}".format(max_depth))
    print(metrics.f1_score(ytest, ypred))
    plt.figure()
    plt.imshow(metrics.confusion_matrix(ypred, ytest),
               interpolation='nearest', cmap=plt.cm.binary)
    plt.colorbar()
    plt.xlabel("true label")
    plt.ylabel("predicted label")
    plt.title("RF: max_depth = {0}".format(max_depth))