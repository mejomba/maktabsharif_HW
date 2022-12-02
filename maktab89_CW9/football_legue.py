from typing import List
import random


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def valid_age(n):
        if int(n) < 0:
            raise ValueError('age cant be negative')
        else:
            return n

    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, value):
    #     if int(value) < 0:
    #         raise ValueError('age cant be negative')
    #     self.__age = value


class Footbalist(Human):
    def __init__(self, name, age, salary, position, rate):
        super().__init__(name, age)
        self.salary = self._valid_salary(salary)
        self.position = position
        self.rate = self._valid_rate(rate)

    @staticmethod
    def valid_age(n):
        if 15 <= int(n) <= 30:
            return n
        else:
            raise ValueError("age between 15 to 30")

    @staticmethod
    def _valid_salary(s):
        if int(s) < 0:
            raise ValueError
        else:
            return s

    @staticmethod
    def _valid_rate(r):
        if 1 < int(r) < 100:
            return r
        else:
            raise ValueError('rate bettwen 1 to 100')

    def __repr__(self):
        return f'{self.name}: {self.position}'


class Couch(Human):
    def __init__(self, name, age, salary, start_date, end_date):
        super().__init__(name, age)
        self.salary = self._valid_salary(salary)
        self.start_date = start_date
        self.end_date = end_date

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 30 <= int(value) <= 65:
            self.__age = value
        else:
            raise ValueError("age between 30 to 65")

    @staticmethod
    def _valid_salary(s):
        if int(s) < 0:
            raise ValueError
        else:
            return s


class Team:
    all_teams = []

    def __init__(self, name, players: List[Footbalist], couch: Couch, balance):
        self.name = name
        self.players = players
        self.couch = couch
        self.point = 0
        self.balance = balance
        self.__class__.all_teams.append(self)

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        if not isinstance(value, list):
            raise TypeError('player must be list of Footbalist')
        if len(value) != 2:
            raise ValueError('length of players 11')
        for player in value:
            if not isinstance(player, Footbalist):
                raise TypeError('all player must be Footbalist')
        self.__players = value

    @property
    def couch(self):
        return self.__couch

    @couch.setter
    def couch(self, value):
        if not isinstance(value, Couch):
            raise TypeError('couch must be Couch')
        for team in self.__class__.all_teams:
            if team.couch.name == value.name:
                raise ValueError("coach not duplicate")
        self.__couch = value

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, value):
        if int(value) < 0:
            raise TypeError('point cant be negative')
        self.__point = value

    def player_count(self):
        return len(self.players)

    @classmethod
    def create_team(cls):
        players_list = []
        name = input('> name: ')
        for _ in range(2):
            data = input('> player: name, age, salary, position, rate').split(' ')
            footbalist = Footbalist(data[0], data[1], data[2], data[3], data[4])
            # footbalist = Footbalist('jafar', 22, 2121, 'fw', 8)
            players_list.append(footbalist)
        couch = input('> Couch: name, age, salary, start_date, end_data').split(' ')
        couch = Couch(name=couch[0], age=couch[1], salary=couch[2], start_date=couch[3], end_date=couch[4])
        balance = input('> team balance: ')
        return cls(name=name, players=players_list, couch=couch, balance=balance)

    def __lt__(self, other):
        return self.point < other.point

    def __gt__(self, other):
        return self.point > other.point

    def __ge__(self, other):
        return self.point >= other.point

    def __le__(self, other):
        return self.point <= other.point

    def __repr__(self):
        return f'{self.name}: {self.point}'


class League:
    def __init__(self, teams: List[Team]):
        self.teams = teams

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, value):
        if len(value) != 3:
            raise ValueError('teams must be 5')
        if not isinstance(value, list):
            raise ValueError("teams must be list of teams")
        for team in value:
            if not isinstance(team, Team):
                raise TypeError('type of teams from Team class')
        self.__teams = value

    def select_team(self):
        return random.sample(self.teams, k=2)

    def match(self):
        team1, team2 = self.select_team()
        shans = random.randint(0, 2)
        if shans == 0:
            team1.point += 1
            team2.point += 1
        elif shans == 1:
            team1.point += 3
        elif shans == 2:
            team2.point += 3

    def ranking(self):
        self.teams.sort(key=lambda x: x.point, reverse=True)
        for team in self.teams:
            print(team)


team1 = Team.create_team()
team2 = Team.create_team()
team3 = Team.create_team()

league1 = League([team1, team2, team3])

for i in range(20):
    league1.match()
    league1.ranking()
    print('='*40)

