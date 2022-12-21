from datetime import datetime


class User:
    user_id = 0

    def __init__(self, username, password, email, role, phone, course):
        self.pk = User.user_id + 1
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.phone = phone
        self.course = course
        self.rates = []


class Score:
    def __init__(self, rate, type_, user):
        self.rate = rate
        self.date = datetime.now()
        self.type = type_
        self.user = user


mojtaba = User('mojtaba', 1234, 'mojtaba@gmail', 'regular', '0936052', 'python')
amin = User('amin', 1234, 'amin@gmail', 'regular', '0936052', 'python')

mojtaba_score1 = Score(20, 'quiz', mojtaba)
mojtaba_score2 = Score(50, 'quiz', mojtaba)
mojtaba_score3 = Score(90, 'excercise', mojtaba)
mojtaba_rates = [mojtaba_score1, mojtaba_score1, mojtaba_score1]

amin_score1 = Score(60, 'excercise', amin)
amin_score2 = Score(70, 'excercise', amin)
amin_score3 = Score(40, 'excercise', amin)
amin_rates = [amin_score1, amin_score2, amin_score3]

Score