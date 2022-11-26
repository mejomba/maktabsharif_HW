import time
import datetime


class BirthDay:
    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def get_age(self):
        current_time = time.time()
        hour = 3600
        day = 24 * hour
        month = 30 * day
        year = 12 * month
        print((current_time / year) + 1970)
        print(((current_time / year) / month) + 1)
        print(datetime.datetime.now())


    def time_to_happy_birth_day(self):
        pass


mojtaba = BirthDay(1991, 6, 7, 22)
mojtaba.get_age()
mojtaba.time_to_happy_birth_day()