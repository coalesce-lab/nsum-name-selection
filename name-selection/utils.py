import pandas as pd
import itertools
import numpy as np
import os.path

def read_data(filepath):
    head, tail = filepath.split('.')
    filepath_ = head + '_.' + tail
    if os.path.isfile(filepath_):
        return pd.read_csv(filepath_)

    data = pd.read_csv(filepath)
    data['count'] = data['count'] / data['count'].sum() * 100

    categories = tuple(col for col in data.columns if col not in ['name', 'count'])
    values = [(c, data[c].unique().astype(str)) for c in categories]
    values_notna = [(c, v) for c, v in values if not 'nan' in v]
    values_na = [(c, v[(v != 'nan')]) for c, v in values if 'nan' in v]
    values = [values_notna + [cv] for cv in values_na] if len(values_na) else [values_notna]
    values = list(map(lambda v: list(zip(*v)), values))
    cross_values = [(c, vv) for c, v in values for vv in itertools.product(*v)]

    alpha = {v[0]: 100 / data['count'][data[v[0]].isna()].sum() for v in values_na}

    category_data = {'name': data['name'].unique()}
    for cat, cross in cross_values:
        column = ','.join(cross)
        category_data[column] = []

        czip = list(zip(cat, cross))
        for n in category_data['name']:
            count = data[np.logical_and.reduce([data['name'] == n] + [data[c] == v for c, v in czip])]['count'].values
            if len(count) == 0:
                count = [0]
            category_data[column].append(count[0])

    vnadict = {k: v for v, keys in values_na for k in keys}
    for k_alpha in alpha.keys():
        for k_cat in category_data.keys():
            if k_cat != 'name':
                if k_alpha == vnadict[k_cat.split(',')[-1]]:
                    category_data[k_cat] = list(map(lambda x: alpha[k_alpha] * x, category_data[k_cat]))

    df = pd.DataFrame(category_data)
    df.to_csv(filepath_, index=False)     
    return df
