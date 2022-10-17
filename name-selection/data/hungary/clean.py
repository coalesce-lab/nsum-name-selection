import pandas as pd

# Read data from excel file
data = pd.read_excel(
    'data.xls',
    sheet_name=None)

# Clean men data

men_1_5 = data['male by age'][['name (1-5 yo)', 'count']].set_axis(['name', 'count'], axis=1).dropna()
men_6_10 = data['male by age'][['name (6-10 yo)', 'count.1']].set_axis(['name', 'count'], axis=1).dropna()
men_11_20 = data['male by age'][['name (11-20 yo)', 'count.2']].set_axis(['name', 'count'], axis=1).dropna()
men_21_30 = data['male by age'][['name (21-30 yo)', 'count.3']].set_axis(['name', 'count'], axis=1).dropna()
men_31_40 = data['male by age'][['name (31-40 yo)', 'count.4']].set_axis(['name', 'count'], axis=1).dropna()
men_41_50 = data['male by age'][['name (41-50 yo)', 'count.5']].set_axis(['name', 'count'], axis=1).dropna()
men_51_60 = data['male by age'][['name (51-60 yo)', 'count.6']].set_axis(['name', 'count'], axis=1).dropna()
men_60_99 = data['male by age'][['name (more than 60)', 'count.7']].set_axis(['name', 'count'], axis=1).dropna()

men_1_5['age'] = '1-5'
men_6_10['age'] = '6-10'
men_11_20['age'] = '11-20'
men_21_30['age'] = '21-30'
men_31_40['age'] = '31-40'
men_41_50['age'] = '41-50'
men_51_60['age'] = '51-60'
men_60_99['age'] = '>60'

clean_data_men = pd.concat([
    men_1_5, men_6_10, men_11_20, men_21_30,
    men_31_40, men_51_60, men_60_99])
clean_data_men.insert(2, 'gender', 'male')

# Clean women data

women_1_5 = data['female by age'][['name (1-5 yo)', 'count']].set_axis(['name', 'count'], axis=1).dropna()
women_6_10 = data['female by age'][['name (6-10 yo)', 'count.1']].set_axis(['name', 'count'], axis=1).dropna()
women_11_20 = data['female by age'][['name (11-20 yo)', 'count.2']].set_axis(['name', 'count'], axis=1).dropna()
women_21_30 = data['female by age'][['name (21-30 yo)', 'count.3']].set_axis(['name', 'count'], axis=1).dropna()
women_31_40 = data['female by age'][['name (31-40 yo)', 'count.4']].set_axis(['name', 'count'], axis=1).dropna()
women_41_50 = data['female by age'][['name (41-50 yo)', 'count.5']].set_axis(['name', 'count'], axis=1).dropna()
women_51_60 = data['female by age'][['name (51-60 yo)', 'count.6']].set_axis(['name', 'count'], axis=1).dropna()
women_60_99 = data['female by age'][['name (more than 60)', 'count.7']].set_axis(['name', 'count'], axis=1).dropna()

women_1_5['age'] = '1-5'
women_6_10['age'] = '6-10'
women_11_20['age'] = '11-20'
women_21_30['age'] = '21-30'
women_31_40['age'] = '31-40'
women_41_50['age'] = '41-50'
women_51_60['age'] = '51-60'
women_60_99['age'] = '>60'

clean_data_women = pd.concat([
    women_1_5, women_6_10, women_11_20, women_21_30,
    women_31_40, women_51_60, women_60_99])
clean_data_men.insert(2, 'gender', 'female')

# Save to csv
clean_data = pd.concat([
    clean_data_men, clean_data_women]).sort_values('count', ascending=False)
clean_data['count'] = clean_data['count'].astype(int)
clean_data = clean_data[clean_data['count'] > 20]

clean_data.to_csv('data.csv', index=False)
