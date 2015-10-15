from matplotlib import pylab as plt
from seasonality import remove_weekday_seasonality


def plot(data, with_weekly_removed=False):
    """
    Plot one data series, grouped already by (channel, country code) key
    :param data: filtered version of data
    :return: None
    """
    dates = data.date
    y = data.user_visits
    plt.plot(dates, y, marker='+', alpha=0.3)
    if with_weekly_removed:
        y_weekly_removed = remove_weekday_seasonality(dates, y)
        plt.plot(dates, y_weekly_removed)


def plot_all_dep(data, with_subplots=True, remove_weekday=False):
    country_codes = list(data.country_code.unique())
    channels = list(data.marketing_channel.unique())
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
                dates = data_one.date
                y = data_one.user_visits
                if remove_weekday:
                    y = remove_weekday_seasonality(dates, y)
                plt.plot(dates, y)
                if with_subplots:
                    title = abrevs[channel] + '_' + country_code
                    plt.title(title)
                    plot_num += 1
