C = np.logspace(-2, 2, 10)
scores = [cross_val_score(SVC(C=Ci), X, y, cv=5, scoring='precision').mean() for Ci in C]
plt.semilogx(C, scores);