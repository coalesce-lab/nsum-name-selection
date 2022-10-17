import pandas as pd
from functools import reduce

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

columns = ['First name'] + [col for col in data_men['German-speaking CH - male'].columns[:-16] if 'J_' in col]
data_men_german = data_men['German-speaking CH - male'][columns]
data_men_german = data_men_german[~data_men_german[columns[1:]].isna().all(axis=1)]
data_men_german = data_men_german.set_axis(['male,german,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

columns = ['First name'] + [col for col in data_men['Italian-speaking CH - male'].columns[:-16] if 'J_' in col]
data_men_italian = data_men['Italian-speaking CH - male'][columns]
data_men_italian = data_men_italian[~data_men_italian[columns[1:]].isna().all(axis=1)]
data_men_italian = data_men_italian.set_axis(['male,italian,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

columns = ['First name'] + [col for col in data_men['French-speaking CH - male'].columns[:-16] if 'J_' in col]
data_men_french = data_men['French-speaking CH - male'][columns]
data_men_french = data_men_french[~data_men_french[columns[1:]].isna().all(axis=1)]
data_men_french = data_men_french.set_axis(['male,french,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

columns = ['First name'] + [col for col in data_men['Romansh-speaking CH - male'].columns[:-16] if 'J_' in col]
data_men_romansh = data_men['Romansh-speaking CH - male'][columns]
data_men_romansh = data_men_romansh[~data_men_romansh[columns[1:]].isna().all(axis=1)]
data_men_romansh = data_men_romansh.set_axis(['male,romansh,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

clean_data_men = reduce(lambda l, r: pd.merge(l, r, how='outer', on='name'), [
    data_men_german, data_men_italian, data_men_french, data_men_romansh])

# Clean women data

columns = ['First name'] + [col for col in data_women['German-speaking CH - female'].columns[:-16] if 'J_' in col]
data_women_german = data_women['German-speaking CH - female'][columns]
data_women_german = data_women_german[~data_women_german[columns[1:]].isna().all(axis=1)]
data_women_german = data_women_german.set_axis(['female,german,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

columns = ['First name'] + [col for col in data_women['Italian-speaking CH - female'].columns[:-16] if 'J_' in col]
data_women_italian = data_women['Italian-speaking CH - female'][columns]
data_women_italian = data_women_italian[~data_women_italian[columns[1:]].isna().all(axis=1)]
data_women_italian = data_women_italian.set_axis(['female,italian,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

columns = ['First name'] + [col for col in data_women['French-speaking CH - female'].columns[:-16] if 'J_' in col]
data_women_french = data_women['French-speaking CH - female'][columns]
data_women_french = data_women_french[~data_women_french[columns[1:]].isna().all(axis=1)]
data_women_french = data_women_french.set_axis(['female,french,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

columns = ['First name'] + [col for col in data_women['Romansh-speaking CH - female'].columns[:-16] if 'J_' in col]
data_women_romansh = data_women['Romansh-speaking CH - female'][columns]
data_women_romansh = data_women_romansh[~data_women_romansh[columns[1:]].isna().all(axis=1)]
data_women_romansh = data_women_romansh.set_axis(['female,romansh,' + col[2:] if 'J_' in col else 'name' for col in columns], axis=1)

clean_data_women = reduce(lambda l, r: pd.merge(l, r, how='outer', on='name'), [
    data_women_german, data_women_italian, data_women_french, data_women_romansh])

# Save to csv
clean_data = pd.merge(clean_data_men, clean_data_women, how='outer', on='name').fillna(0)

alpha = 100 / clean_data.sum(numeric_only=True).sum()
for c in clean_data.columns[1:]:
    clean_data[c] = alpha * clean_data[c]

clean_data.to_csv('data_.csv', index=False)
