import datetime

from config import TODAY, RANGE, DATE_FORMAT


class Knowledge:
    def __init__(self, name, start_day=TODAY):
        self.name = name
        self.start_day = start_day

        self.dates = []

        self.generate_dates()

    def generate_dates(self):
        if isinstance(self.start_day, str):
            self.start_day = datetime.datetime.strptime(self.start_day, DATE_FORMAT)

        for i in range(len(RANGE)):
            self.dates.append(self.start_day + datetime.timedelta(days=RANGE[i]))
