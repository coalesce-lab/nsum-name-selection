import pandas as pd

# Read data from csv file
data = pd.read_csv('poland.csv')

# Clean data

data = data[['name', 'n', 'gender', 'year']].set_axis(['name', 'count', 'gender', 'year'], axis=1)
data = data.sort_values(['year', 'count'], ascending=False)
data = data[(data['year'] == 2022) & (data['count'] > 20)].drop('year', axis=1)

# Save to csv
data.to_csv('data.csv', index=False)
