import pandas as pd

# Read data from excel file
data = pd.read_excel(
    'data.xls',
    sheet_name=None,
    header=3,
    na_values='..')

# Clean men data

data_men_year = [
    (data['Table 1 Men'][['Name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[5:])
    for col in data['Table 1 Men'].columns if 'Born' in col]

for d, year in data_men_year:
    d['year'] = year

data_men_county = [
    (data['Table 2 Men'][['Name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[:-7])
    for col in data['Table 2 Men'].columns if 'County' in col]

for d, county in data_men_county:
    d['county'] = county

clean_data_men = pd.concat(
    [d for d, _ in data_men_year] +
    [d for d, _ in data_men_county])
clean_data_men.insert(2, 'gender', 'male')

# Clean women data

data_women_year = [
    (data['Table 1 Women'][['Name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[5:])
    for col in data['Table 1 Women'].columns if 'Born' in col]

for d, year in data_women_year:
    d['year'] = year

data_women_county = [
    (data['Table 2 Women'][['Name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[:-7])
    for col in data['Table 2 Women'].columns if 'County' in col]

for d, county in data_women_county:
    d['county'] = county

clean_data_women = pd.concat(
    [d for d, _ in data_women_year] +
    [d for d, _ in data_women_county])
clean_data_women.insert(2, 'gender', 'women')

# Save to csv
clean_data = pd.concat([
    clean_data_men, clean_data_women]).sort_values('count', ascending=False)
clean_data['count'] = clean_data['count'].astype(int)
clean_data = clean_data[clean_data['count'] > 20]

clean_data.to_csv('data.csv', index=False)
