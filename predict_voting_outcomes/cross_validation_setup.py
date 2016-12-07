"""
Split the dataset into training and test set with split being (80, 20)
Cross-validation will choose random people from the training set and do so
for k-different folds.
"""

from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import StratifiedKFold

def split_dataset(X, y):
	Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, \
		                 test_size=0.2, random_state=1221)

	return (Xtr, Xte, ytr, yte)

def perform_cross_validation(X, y, est):
	cv = StratifiedKFold(y, n_folds=5, random_state=1231)
	cv_scores = cross_val_score(est, X, y, cv=cv, scoring='accuracy', n_jobs=-1)

	return cv_scores

def perform_cross_validation_multiple(X, y, estimators, ensemble=False):
	for est_name, model in estimators:
		cv_scores = perform_cross_validation(X, y, model)
		print('Accuracy score for: %s is: %f and std: %f'%(est_name, cv_scores.mean(), cv_scores.std()))
