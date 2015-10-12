import pandas as pd

data_dir = 'data'


def read(name='visits'):
    filename = "%s/%s.csv" % (data_dir, name)
    data = pd.read_csv(filename)
    data['date'] = pd.to_datetime(data.datestamp)
    del data['datestamp']
    data.set_index('date')
    return data




