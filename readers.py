import pandas as pd

data_dir = 'data'


def channel_abbrevs():
    names = ['Display Ads', 'KAYAK Deals Email', 'Search Engine Ads', 'Search Engine Results', 'Travel Search Site']
    abrev = ['Disp', 'Deals', 'SEA', 'SER', 'TS']
    return dict(zip(names, abrev))


def read(name='visits'):
    """
    :param name: visits (default) or conversions
    :return: data read from file with added fields
             pandas DataFrame
    """
    filename = "%s/%s.csv" % (data_dir, name)
    data = pd.read_csv(filename)
    data['date'] = pd.to_datetime(data.datestamp)
    del data['datestamp']
    abbrevs = channel_abbrevs()
    data['channel'] = [abbrevs[channel]
                       for channel in data.marketing_channel]
    data['key'] = data.channel + '_' + data.country_code
    data.set_index('date')
    return data


def read_merged():
    """
    Read vists and conversions file and merge them
    :return: merged data frame
    """
    # Laplace prior on ratios
    alpha = 1.0
    prior = 0.3
    visits = read('visits')
    conversions = read('conversions')
    # inner join on date
    merged = visits.merge(conversions)
    n_visits = len(visits)
    n_conversions = len(conversions)
    n_merged = len(merged)
    numerator = (merged['conversions'] + alpha)
    denom = (merged['user_visits'] + alpha/prior)
    merged['conversion_rate'] = numerator/denom
    merged = merged[merged.conversion_rate < 1]
    n_final = len(merged)
    n_bad = n_merged - n_final
    print 'n_visits: %s, n_conversions: %s, merged: %s, n_bad: %s, n_final: %s' \
          % (n_visits, n_conversions, n_merged, n_bad, n_final)
    return merged





