import numpy as np
import pandas as pd

def missing_value_features(data):
	# count how many features are missing for a record
	data['missing_val_count'] = data.apply(lambda x: pd.isnull(x).sum(), axis=1)
	return data

def create_age(yob):
	if yob != -9999:
		return 2016 - yob
	else:
		return -9999

def create_age_mapping(age):
	if age < 17:
		return 0
	elif age >= 18 and age < 25:
		return 1
	elif age >= 25 and age < 35:
		return 2
	elif age >= 35 and age < 50:
		return 3
	elif age >= 50 and age < 65:
		return 4
	elif age >= 65:
		return 5
	else:
		return -9999

def remove_outliers(data):
	mask = (data.Party.notnull()) & ((data.Age < 18) | (data.Age > 90))
	data = data.iloc[(np.where(~mask))]

	return data
