import time

# time.ctime(sec) -> ['Sun', 'Nov', '27', '10:37:15', '2022']
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


class BirthDay:
    def __init__(self, year, month, day, hour):
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
            now_day_of_month = now_day_of_month - 1
            now_hour += 24

        if now_day_of_month - self.day < 0:
            now_month = now_month - 1
            now_day_of_month = now_day_of_month + 30

        if now_month - self.month < 0:
            now_year = now_year - 1
            now_month = now_month + 12

        now = [now_year, now_month, now_day_of_month, now_hour]
        user_birth_day = [self.year, self.month, self.day, self.hour]
        hint = ['year', 'month', 'day', 'hour']

        result = []
        for h, current, user_birth in zip(hint, now, user_birth_day):
            result.append((h, current - user_birth))

        return result

    def time_to_happy_birth_day(self):
        month, day, hour = self.get_age()[1:]
        return [("months", 12 - month[1]), ("day", 30 - day[1]), ("hour",24 - hour[1])]


mojtaba = BirthDay(year=1991, month=11, day=20, hour=19)

age = mojtaba.get_age()
print(age)
time_to_birthday = mojtaba.time_to_happy_birth_day()
print(time_to_birthday)
