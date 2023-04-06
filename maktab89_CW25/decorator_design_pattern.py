# class Character:
#     def __init__(self) -> None:
#         self.health = 500

#     def get_health(self):
#         return self.health
    

# class HealthBuff(Character):
#     def __init__(self, hero, buff) -> None:
#         super(HealthBuff, self).__init__()
#         self.hero = hero
#         self.buff = buff

#     def get_health(self):
#         hero_health = self.hero.get_health()
#         hero_health += self.buff.get_power()
#         return hero_health
    
# class Buff:
#     def __init__(self) -> None:
#         self.power = 100
    
#     def get_power(self):
#         return self.power
    
# John = Character()
# healthy = Buff()
# print(John.get_health())

# John = HealthBuff(John, healthy)

# print(John.get_health())

class Coffe:
    def __init__(self) -> None:
        self.cost = 100

    def get_cost(self):
        return self.cost
    
class CoffeDecorator(Coffe):
    def __init__(self, coffe, additional) -> None:
        super(CoffeDecorator, self).__init__()
        self.coffe = coffe
        self.additional = additional

    def get_cost(self):
        coffe_cost = self.coffe.get_cost()
        coffe_cost += self.additional.get_cost()
        return coffe_cost
    
class Additional:
    def __init__(self, cost) -> None:
        self.cost = cost

    def get_cost(self):
        return self.cost

arabica = Coffe()
mocha = Additional(50)
suger = Additional(10)
print(arabica.get_cost())
arabica = CoffeDecorator(arabica, mocha)
arabica = CoffeDecorator(arabica, suger)
print(arabica.get_cost())