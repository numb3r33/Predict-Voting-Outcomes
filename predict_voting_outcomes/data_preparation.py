from sklearn.preprocessing import LabelEncoder

def fill_missing_values(df):
	df = df.copy()

	for cat in df.columns:
		if cat == 'Party':
			continue
		if df[cat].isnull().any():
			if df[cat].dtype == 'object':
				df[cat] = df[cat].fillna('-999')
			else:
				df[cat] = df[cat].fillna(-9999)
	return df

def encode_cat_features(df):
	df = df.copy()

	for cat in df.columns:
		if cat == 'Party':
			continue
		if df[cat].dtype == 'object':
			lbl = LabelEncoder()

			lbl.fit(df[cat])
			df[cat] = lbl.transform(df[cat])

	return df
