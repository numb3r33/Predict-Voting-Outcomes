from sklearn.preprocessing import LabelEncoder


def preprocess_process_1(data):
	"""
	Fill missing values with -9999 and
	encode all the categorical variables.
	"""
	data = fill_missing_values(data)
	data = encode_cat_features(data)

	return data

def preprocess_process_2(data):
	"""
	Fill missing values with most common value and create a
	separate variable that stores whether value was missing or not.
	"""

	data = fill_missing_values_with_flag(data)
	data = encode_cat_features(data)

	return data



def fill_missing_values(df):
	"""
	Fill categorical value with -9999
	"""

	for cat in df.columns:
		if cat == 'Party':
			continue
		if df[cat].isnull().any():
			if df[cat].dtype == 'object':
				df[cat] = df[cat].fillna('-999')
			else:
				df[cat] = df[cat].fillna(-9999)
	return df

def fill_missing_values_with_flag(df):

	"""
	Fill missing value with the most common column
	for a particular feature and create a separate feature
	which would mark which all entries were imputed.
	"""

	for col in df.columns:
		if col == 'Party':
			continue

		if df[col].isnull().any():
			df[col + '_missing'] = df[col].isnull().astype(int)
			df[col] = df[col].fillna(df[col].value_counts().argmax())

	return df

def encode_cat_features(df):
	"""
	Encode categorical variables with Label Encoder
	"""
	for cat in df.columns:
		if cat == 'Party':
			continue
		if df[cat].dtype == 'object':
			lbl = LabelEncoder()

			lbl.fit(df[cat])
			df[cat] = lbl.transform(df[cat])

	return df
