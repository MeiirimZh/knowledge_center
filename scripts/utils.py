import datetime

from config import DATE_FORMAT


def convert_dates_to_strings(dates):
    converted_dates = []
    for date in dates:
        converted_dates.append(datetime.datetime.strftime(date, DATE_FORMAT))
    return converted_dates
