from sklearn.ensemble import RandomForestRegressor
X, y = make_data(500, error=1)

clf = RandomForestRegressor(10)
max_depth = np.arange(1, 10)

grid = GridSearchCV(clf, param_grid={'max_depth': max_depth},
                    scoring='mean_squared_error', cv=5)
grid.fit(X, y)

scores = [g[1] for g in grid.grid_scores_]
plt.plot(max_depth, scores);