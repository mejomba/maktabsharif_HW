from models import Product, User
from functools import reduce
import itertools


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()
        # print(self.products)
        # print(self.users)

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        number_of_product = self.products.get(product)
        if not number_of_product:
            raise Exception('Not Enough Products')
        elif number_of_product == 0:
            self.products.pop(product)
        elif 0 < number_of_product < amount:
            self.products[product] = number_of_product - amount
        # else:
        #     raise Exception('Not Enough Products')

    def add_user(self, username):
        for user in self.users:
            if username == user.username:
                return
        user = User(username)
        self.users.append(user)
        return user.username

    def get_total_asset(self):

        # return reduce(lambda x, y: x + y, map(lambda x: x.price, self.products))
        sum_of_price = 0
        for product in self.products:
            sum_of_price += product.price
        return sum_of_price

    def get_total_profit(self):
        sum_of_profit = 0
        for user in self.users:
            for product in user.bought_products:
                sum_of_profit += product.price
        return sum_of_profit

    def get_comments_by_user(self, user):
        user_comment = list()
        for product in self.products:
            for comment in product.comments:
                if comment.user.username == user.username:
                    user_comment.append(comment)
        return user_comment

    def get_inflation_affected_product_names(self):
        inflation_list = list()
        product_list = list(self.products)
        product_name_and_price = []
        print(product_list)
        copy_product = self.products.copy()

        for p in product_list:
            product_name_and_price.append((p.name, p.price))
        out = itertools.compress(product_name_and_price, filter(lambda x, y: x[0] == y[0] and x[1] != y[1], product_name_and_price))
        print(list(out))
        # out = filter(lambda x: x[0] == y[0] and x[1] != y[1], product_name_and_price)
        # for item in out:
        #     print(item)
        # return list(map(lambda x, : (x[0], x[1]), product_name_and_price))
        # return product_name_and_price

        # while copy_product:
        #     for product in self.products:
        #         pass
        # if item not in inflation_list:
        #     inflation_list.append(item)

        # print(copy_product.popitem()[0])
        # return list(filter(lambda x: x.name == copy_product.popitem()[0].name, self.products))

    def clean_old_comments(self, date):
        for product in self.products:
            product.comments = [comment for comment in product.comments if comment.date_added > date]

    def get_comments_by_bought_users(self, product):
        list_of_comments_by_bought_users = list()
        for comment in product.comments:
            for user in comment.user:
                for p in user.bought_products:
                    if p.id == product.id:
                        list_of_comments_by_bought_users.append(comment)
        return list_of_comments_by_bought_users

        # for user in self.users:
        #     for user_product in user.bought_products:
        #         if user_product.id == product.id:
        #             return product.comments


p1 = Product('name1', 2000, 'c1')
p2 = Product('name1', 3000, 'c1')
p3 = Product('name3', 3000, 'c1')
p4 = Product('name3', 3000, 'c1')
s1 = Store()
Store.add_product(s1, p1)
Store.add_product(s1, p2)
Store.add_product(s1, p3)
Store.add_product(s1, p4)
print(s1.products)
print(s1.get_inflation_affected_product_names())