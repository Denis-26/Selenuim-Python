import datetime
from datetime import timedelta


class DateHelper:

    def __init__(self, template):
        self.template = template

    def two_dates_delta(self, start, end):
        start = datetime.datetime.strptime(start, self.template)
        end = datetime.datetime.strptime(end, self.template)
        end += timedelta(days=1)
        return (end - start).days

