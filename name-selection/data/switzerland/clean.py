import pandas as pd

# Read data from excel file
data_men = pd.read_excel(
    'data_male.xls',
    sheet_name=None,
    header=2,
    na_values='*')

data_women = pd.read_excel(
    'data_female.xls',
    sheet_name=None,
    header=2,
    na_values='*')

# Clean men data

data_men_german = [
    (data_men['German-speaking CH - male'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_men['German-speaking CH - male'].columns[:-16] if 'J_' in col]

for d, year in data_men_german:
    d['year'] = year
    d['language'] = 'german'

data_men_italian = [
    (data_men['Italian-speaking CH - male'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_men['Italian-speaking CH - male'].columns[:-16] if 'J_' in col]

for d, year in data_men_italian:
    d['year'] = year
    d['language'] = 'italian'

data_men_french = [
    (data_men['French-speaking CH - male'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_men['French-speaking CH - male'].columns[:-16] if 'J_' in col]

for d, year in data_men_french:
    d['year'] = year
    d['language'] = 'french'

data_men_romansh = [
    (data_men['Romansh-speaking CH - male'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_men['Romansh-speaking CH - male'].columns[:-16] if 'J_' in col]

for d, year in data_men_romansh:
    d['year'] = year
    d['language'] = 'romansh'

clean_data_men = pd.concat(
    [d for d, _ in data_men_german] +
    [d for d, _ in data_men_italian] +
    [d for d, _ in data_men_french] +
    [d for d, _ in data_men_romansh])
clean_data_men.insert(2, 'gender', 'male')

# Clean women data

data_women_german = [
    (data_women['German-speaking CH - female'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_women['German-speaking CH - female'].columns[:-16] if 'J_' in col]

for d, year in data_women_german:
    d['year'] = year
    d['language'] = 'german'

data_women_italian = [
    (data_women['Italian-speaking CH - female'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_women['Italian-speaking CH - female'].columns[:-16] if 'J_' in col]

for d, year in data_women_italian:
    d['year'] = year
    d['language'] = 'italian'

data_women_french = [
    (data_women['French-speaking CH - female'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_women['French-speaking CH - female'].columns[:-16] if 'J_' in col]

for d, year in data_women_french:
    d['year'] = year
    d['language'] = 'french'

data_women_romansh = [
    (data_women['Romansh-speaking CH - female'][['First name', col]].set_axis(['name', 'count'], axis=1).dropna(), col[2:])
    for col in data_women['Romansh-speaking CH - female'].columns[:-16] if 'J_' in col]

for d, year in data_women_romansh:
    d['year'] = year
    d['language'] = 'romansh'

clean_data_women = pd.concat(
    [d for d, _ in data_women_german] +
    [d for d, _ in data_women_italian] +
    [d for d, _ in data_women_french] +
    [d for d, _ in data_women_romansh])
clean_data_women.insert(2, 'gender', 'female')

# Save to csv
clean_data = pd.concat([
    clean_data_men, clean_data_women]).sort_values('count', ascending=False)
clean_data['count'] = clean_data['count'].astype(int)

clean_data.to_csv('data.csv', index=False)
