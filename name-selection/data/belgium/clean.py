import pandas as pd

# Read data from excel file
data = pd.read_excel(
    'data.xls',
    sheet_name=None,
    header=[0, 1])

# Clean men data
flanders = data['Men'].xs('Flanders', axis=1)
wallonia = data['Men'].xs('Wallonia', axis=1)
brussels = data['Men'].xs('Brussels', axis=1)

flanders_18 = flanders[['Younger than 18.1', '#']].set_axis(['name', 'count'], axis=1).dropna()
flanders_64 = flanders[['Between 18 and 64.1', '#.1']].set_axis(['name', 'count'], axis=1).dropna()
flanders_65 = flanders[['65 and older.1', '#.2']].set_axis(['name', 'count'], axis=1).dropna()

wallonia_18 = wallonia[['Younger than 18.1', '#']].set_axis(['name', 'count'], axis=1).dropna()
wallonia_64 = wallonia[['Between 18 and 64.1', '#.1']].set_axis(['name', 'count'], axis=1).dropna()
wallonia_65 = wallonia[['65 and older.1', '#.2']].set_axis(['name', 'count'], axis=1).dropna()

brussels_18 = brussels[['Younger than 18.1', '#']].set_axis(['name', 'count'], axis=1).dropna()
brussels_64 = brussels[['Between 18 and 64.1', '#.1']].set_axis(['name', 'count'], axis=1).dropna()
brussels_65 = brussels[['65 and older.1', '#.2']].set_axis(['name', 'count'], axis=1).dropna()

flanders_18['area'] = 'flanders'
flanders_64['area'] = 'flanders'
flanders_65['area'] = 'flanders'
wallonia_18['area'] = 'wallonia'
wallonia_64['area'] = 'wallonia'
wallonia_65['area'] = 'wallonia'
brussels_18['area'] = 'brussels'
brussels_64['area'] = 'brussels'
brussels_65['area'] = 'brussels'

flanders_18['age'] = '0-17'
flanders_64['age'] = '18-64'
flanders_65['age'] = '65-inf'
wallonia_18['age'] = '0-17'
wallonia_64['age'] = '18-64'
wallonia_65['age'] = '65-inf'
brussels_18['age'] = '0-17'
brussels_64['age'] = '18-64'
brussels_65['age'] = '65-inf'

clean_data_men = pd.concat([
    flanders_18, flanders_64, flanders_65,
    wallonia_18, wallonia_64, wallonia_65,
    brussels_18, brussels_64, brussels_65])
clean_data_men.insert(2, 'gender', 'male')

# Clean women data
flanders = data['Women'].xs('Flanders', axis=1)
wallonia = data['Women'].xs('Wallonia', axis=1)
brussels = data['Women'].xs('Brussels', axis=1)

flanders_18 = flanders[['Younger than 18.1', '#']].set_axis(['name', 'count'], axis=1).dropna()
flanders_64 = flanders[['Between 18 and 64.1', '#.1']].set_axis(['name', 'count'], axis=1).dropna()
flanders_65 = flanders[['65 and older.1', '#.2']].set_axis(['name', 'count'], axis=1).dropna()

wallonia_18 = wallonia[['Younger than 18.1', '#']].set_axis(['name', 'count'], axis=1).dropna()
wallonia_64 = wallonia[['Between 18 and 64.1', '#.1']].set_axis(['name', 'count'], axis=1).dropna()
wallonia_65 = wallonia[['65 and older .1', '#.2']].set_axis(['name', 'count'], axis=1).dropna() # Added U+00a0 to name to correct mistake in xls

brussels_18 = brussels[['Younger than 18.1', '#']].set_axis(['name', 'count'], axis=1).dropna()
brussels_64 = brussels[['Between 18 and 64.1', '#.1']].set_axis(['name', 'count'], axis=1).dropna()
brussels_65 = brussels[['65 and older.1', '#.2']].set_axis(['name', 'count'], axis=1).dropna()

flanders_18['area'] = 'flanders'
flanders_64['area'] = 'flanders'
flanders_65['area'] = 'flanders'
wallonia_18['area'] = 'wallonia'
wallonia_64['area'] = 'wallonia'
wallonia_65['area'] = 'wallonia'
brussels_18['area'] = 'brussels'
brussels_64['area'] = 'brussels'
brussels_65['area'] = 'brussels'

flanders_18['age'] = '0-17'
flanders_64['age'] = '18-64'
flanders_65['age'] = '65-inf'
wallonia_18['age'] = '0-17'
wallonia_64['age'] = '18-64'
wallonia_65['age'] = '65-inf'
brussels_18['age'] = '0-17'
brussels_64['age'] = '18-64'
brussels_65['age'] = '65-inf'

clean_data_women = pd.concat([
    flanders_18, flanders_64, flanders_65,
    wallonia_18, wallonia_64, wallonia_65,
    brussels_18, brussels_64, brussels_65])
clean_data_women.insert(2, 'gender', 'female')

# Save to csv
clean_data = pd.concat([
    clean_data_men, clean_data_women]).sort_values('count', ascending=False)
clean_data['count'] = clean_data['count'].astype(int)
clean_data = clean_data[clean_data['count'] > 20]

clean_data.to_csv('data.csv', index=False)
