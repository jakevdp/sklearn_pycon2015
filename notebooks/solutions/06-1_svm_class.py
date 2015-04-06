from sklearn.svm import SVC
# First instantiate the "Support Vector Classifier" (SVC) model
clf = SVC()

# Next split the data (X and y) into a training and test set
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)

# fit the model to the training data
clf.fit(Xtrain, ytrain)

# compute y_pred, the predicted labels of the test data
ypred = clf.predict(Xtest)

# Now that this is finished, we'll compute the classification rate
print "accuracy:", np.sum(ytest == ypred) * 1. / len(ytest)