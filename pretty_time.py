import time
from datetime import datetime


class PrettyTime:
    def __init__(self, upper_date: str, bottom_date: str):
        super().__init__()
        self.raw_timestamps = [upper_date, bottom_date]
        self.list_of_dt = self.set_timestamps()

    def convert_timestamp(self, ts, from_pattern, to_pattern):
        return datetime.strptime(ts, from_pattern)

    def set_timestamps(self):
        return [self.convert_timestamp(ts, '%Y-%m-%d %H:%M:%S', '%m-%d-%Y')
                for ts in self.raw_timestamps]
