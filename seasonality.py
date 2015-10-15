from collections import defaultdict, Counter


def average_by_weekday(dates, y):
    """
    :param dates: list or Series of dates
    :param y: list or Series of some time-series numerical value
    :return: dictionary of weekday averages
             and global average, keyed by 'all'
    """
    assert len(dates) == len(y)
    weekdays = [date.to_pydatetime().weekday() for date in dates]
    sum_by_weekday = defaultdict(float)
    num_weekdays = Counter()
    for weekday, y_value in zip(weekdays, y):
        sum_by_weekday[weekday] += float(y_value)
        num_weekdays[weekday] += 1
    averages = {k: v/float(num_weekdays[k])
                for k, v in sum_by_weekday.iteritems()}
    average_all = y.mean()
    averages['all'] = average_all
    return averages


def remove_weekday_seasonality(dates, y):
    """
    :param dates: list or Series of dates
    :param y: list or Series of some time-series numerical value
    :return: same value with the weekday seasonality subtracted
             (but same global average)
    """
    avg_by_weekday = average_by_weekday(dates, y)
    avg = avg_by_weekday['all']
    return [avg*y_value/avg_by_weekday[d.to_pydatetime().weekday()]
            for d, y_value in zip(dates, y)]
