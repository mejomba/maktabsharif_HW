import time

# time.ctime(sec).split(" ") -> ['Sun', 'Nov', '27', '10:37:15', '2022']
months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}


class YearException(Exception):
    def __init__(self, message='year must be positive'):
        self.message = message
        super().__init__(self.message)


class MonthException(Exception):
    def __init__(self, message='month must be 1 to 12'):
        self.message = message
        super().__init__(self.message)


class DayException(Exception):
    def __init__(self, message='day must be 1 to 31'):
        self.message = message
        super().__init__(self.message)


class HourException(Exception):
    def __init__(self, message='hour must be 0 to 23'):
        self.message = message
        super().__init__(self.message)


class BirthDay:
    def __init__(self, year, month, day, hour):

        if not year > 0:
            raise YearException
        if not 1 <= month <= 12:
            raise MonthException
        if not 1 <= day <= 31:
            raise DayException
        if not 0 <= hour <= 23:
            raise HourException

        # assert year > 0, 'year must be positive'
        # assert 1 <= month <= 12, 'month must be 1 to 12'
        # assert 1 <= day <= 31, 'day must be 1 to 31'
        # assert 0 <= hour <= 23, 'hour must be 0 to 23'
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def get_age(self):
        _, now_month_name, now_day_of_month, now_clock, now_year = time.ctime(time.time()).split(' ')
        now_hour, _, _ = now_clock.split(':')
        now_month = months[now_month_name]

        now_year = int(now_year)
        now_month = int(now_month)
        now_day_of_month = int(now_day_of_month)
        now_hour = int(now_hour)

        if now_hour - self.hour < 0:
            now_day_of_month -= 1
            now_hour += 24

        if now_day_of_month - self.day < 0:
            now_month -= 1
            now_day_of_month += 30

        if now_month - self.month < 0:
            now_year -= 1
            now_month += 12

        user_birth_day = [self.year, self.month, self.day, self.hour]
        now = [now_year, now_month, now_day_of_month, now_hour]
        hint = ['year', 'month', 'day', 'hour']

        result = []
        for h, current, user_birth in zip(hint, now, user_birth_day):
            result.append((h, current - user_birth))

        return result

    def time_to_happy_birth_day(self):
        month, day, hour = self.get_age()[1:]
        return [(month[0], 11 - month[1]), (day[0], 30 - day[1]), (hour[0], 24 - hour[1])]


mojtaba = BirthDay(year=1993, month=4, day=7, hour=7)

age = mojtaba.get_age()
for item in age:
    print(*item)
print('=' * 20)
time_to_birthday = mojtaba.time_to_happy_birth_day()
for item in time_to_birthday:
    print(*item)

