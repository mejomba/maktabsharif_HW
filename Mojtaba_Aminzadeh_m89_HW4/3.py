class BankAccount:
    def __init__(self, name: str, amount: int) -> None:
        try:
            assert amount >= 1000, "minimum value 1000"
            self.name = name
            self.amount = amount
            self.__min_amount = 1000
        except AssertionError as e:
            print(e)

    def withdraw(self, value: int):
        try:
            assert isinstance(value, int), "invalid withdraw value. expect int"
            assert value <= self.amount - self.__min_amount, "you not enough money"
            assert value > 0, f"withdraw value can't be {value}"
            self.amount -= value
        except AssertionError as e:
            print(e)

    def deposit(self, value: int):
        try:
            assert isinstance(value, int), "invalid deposit value. expect int"
            assert value > 0, f"deposit value can't be {value}"
            self.amount += value
        except AssertionError as e:
            print(e)

    def transaction(self, other: 'BankAccount', value: int):
        try:
            assert isinstance(other, BankAccount), "invalid account"
            assert  isinstance(value, int), "invalid transaction value"
            assert value > 0, f"transaction value can't be {value}"
            self.amount -= value
            other.amount += value
        except AssertionError as e:
            print(e)


mojtaba_acc = BankAccount('mojtaba', 4500)
mamad_acc = BankAccount('mamad', 8000)


mojtaba_acc.deposit(1000)
print(mojtaba_acc.amount)
mojtaba_acc.transaction(mamad_acc, 1200)
print(mojtaba_acc.amount)
print(mamad_acc.amount)

