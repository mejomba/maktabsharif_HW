from models import Product, User, Comment


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        number_of_product = self.products.get(product)
        if number_of_product < amount:
            raise Exception('Not Enough Products')

        elif number_of_product == 0:
            self.products.pop(product)
        elif 0 < number_of_product >= amount:
            self.products[product] = number_of_product - amount

        number_of_product = self.products.get(product)
        if number_of_product == 0:
            self.products.pop(product)

    def add_user(self, username):
        for user in self.users:
            if username == user.username:
                return
        user = User(username)
        self.users.append(user)
        return user.username

    def get_total_asset(self):
        sum_of_price = 0
        for product in self.products:
            mac = product.price * self.products.get(product)
            sum_of_price += mac
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
                    user_comment.append(comment.text)
        return user_comment

    def get_inflation_affected_product_names(self):
        inflation_list = list()
        copy_product = self.products.copy()

        product_name_and_price = [(p.name, p.price) for p in self.products]

        while copy_product:
            item = copy_product.popitem()
            name, price = item[0].name, item[0].price
            print(name, price)
            for p_name, p_price in product_name_and_price:
                if name == p_name and price != p_price:
                    inflation_list.append(name)

        return list(set(inflation_list))

    def clean_old_comments(self, date):
        for product in self.products:
            product.comments = [comment for comment in product.comments if comment.date_added > date]

    def get_comments_by_bought_users(self, product):
        list_of_comments_by_bought_users = list()
        for user in self.users:
            for user_bought_product in user.bought_products:
                if user_bought_product.name == product.name:
                    for comment in user_bought_product.comments:
                        if user == comment.user:
                            list_of_comments_by_bought_users.append(comment.text)
        return list_of_comments_by_bought_users
