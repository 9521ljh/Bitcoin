import pandas as pd

df = pd.read_csv('1d.csv')

dict_ = {'symbol': 'AAPL'}
# subdict = {'symbol': 'AAPL'}
klines = []
for idx in range(len(df)):
    klines.append({
        'datetime': str(df.iloc[idx]['datetime']),
        'open' : float(df.iloc[idx]['open']),
        'high' : float(df.iloc[idx]['high']),
        'low' : float(df.iloc[idx]['low']),
        'close' : float(df.iloc[idx]['close']),
        'volume' : float(df.iloc[idx]['volume']),        
    })
    dict_.update({'klines': klines})

import json

with open('AAPL_datetime.json', 'w') as fp:
    json.dump(dict_, fp)