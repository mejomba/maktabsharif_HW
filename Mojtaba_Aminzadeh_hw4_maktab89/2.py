import time

# time.ctime(sec).split("") -> ['Sun', 'Nov', '27', '10:37:15', '2022']
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

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def get_age(self) -> list:
        _, now_month_name, now_day_of_month, now_clock, now_year = time.ctime(time.time()).split()
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
        for h, current_time, user_birth in zip(hint, now, user_birth_day):
            result.append((h, current_time - user_birth))

        year_in_hour = result[0][1] * 8760  # one year in hour  = 8760 (base on 365 day)
        month_in_hour = result[1][1] * 720  # one month in hour = 720 (base on 30 day)
        day_in_hour = result[2][1] * 24     # one day in hour   = 24 (base on 1 day)
        hour_in_hour = result[3][1]         # one hour in hour
        age_in_hour = ('age in hour:', year_in_hour + month_in_hour + day_in_hour + hour_in_hour)
        result.append(age_in_hour)

        return result

    def time_to_happy_birth_day(self) -> list:
        result = []
        month, day, hour = self.get_age()[1:-1]  # get => month, day, hour with "hint"

        month_to_birth_day, day_to_birth_day, hour_to_birth_day = [(month[0], 11 - month[1]), (day[0], 30 - day[1]), (hour[0], 24 - hour[1])]
        month_hour = month_to_birth_day[1] * 720  # one month in hour = 720 (base on 30 day)
        day_hour = day_to_birth_day[1] * 24       # one day in hour   = 24 (base on 1 day)
        hour_hour = hour_to_birth_day[1]          # one hour in hour
        to_birth_day_in_hour = ('time_to_birth_day in hour:', month_hour + day_hour + hour_hour)

        result.append(month_to_birth_day)
        result.append(day_to_birth_day)
        result.append(hour_to_birth_day)
        result.append(to_birth_day_in_hour)

        return result


mojtaba = BirthDay(year=1993, month=4, day=7, hour=7)

age = mojtaba.get_age()
for item in age:
    print(*item)

print('=' * 25, 'time to birth day')
time_to_birthday = mojtaba.time_to_happy_birth_day()
for item in time_to_birthday:
    print(*item)
