from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
digits = load_digits()
X, y = digits.data, digits.target

# construct the K Neighbors classifier
knn = KNeighborsClassifier()

# Use GridSearchCV to find the best accuracy given choice of ``n_neighbors``
n_neighbors = np.arange(1, 10)
grid = GridSearchCV(knn, param_grid={'n_neighbors': n_neighbors},
                    scoring='precision', cv=5)
grid.fit(X, y)
print "best parameter choice:", grid.best_params_

# Plot the accuracy as a function of the number of neighbors.
# Does this change significantly if you use more/fewer folds?
scores = [g[1] for g in grid.grid_scores_]
plt.plot(n_neighbors, scores);