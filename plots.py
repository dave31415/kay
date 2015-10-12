from matplotlib import pylab as plt


def channel_abbrevs():
    names = ['Display Ads', 'KAYAK Deals Email', 'Search Engine Ads', 'Search Engine Results', 'Travel Search Site']
    abrev = ['Disp', 'Deals', 'SEA', 'SER', 'TS']
    return dict(zip(names, abrev))


def plot_all(data, with_subplots = True):
    country_codes = list(data.country_code.unique())
    channels = list(data.marketing_channel.unique())
    print 'Country codes'
    print country_codes
    print 'Channels'
    print channels
    ny = len(country_codes)
    nx = len(channels)
    plot_num = 1

    abrevs = channel_abbrevs()

    for channel in channels:
        for country_code in country_codes:
            data_one = data[(data.country_code == country_code)
                            & (data.marketing_channel == channel)]
            if len(data_one) > 2:
                if with_subplots:
                    plt.subplot(nx, ny, plot_num)
                plt.plot(data_one.date, data_one.user_visits)
                if with_subplots:
                    title = abrevs[channel] + '_' + country_code
                    plt.title(title)
                    plot_num += 1
