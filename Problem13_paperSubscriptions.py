SUBSCRIPTION_PRICE = 50

class Problem13():
    def __init__(self, name, subscription_price=SUBSCRIPTION_PRICE):
        self._name = name
        self._subscription_price = SUBSCRIPTION_PRICE
        self.depositAmt = 0
        self.subscription_years = []

    def add_subscription(self, year):
        self.subscription_years.append(year)
        # print(self.subscription_years)
        return self.subscription_years

    def subscribe(self, year):
        if self.depositAmt >= self._subscription_price:
            self.add_subscription(year)
            self.depositAmt -= self._subscription_price
            print("subscription successful for year", year, "for user", self._name)
        else:
            print("insufficient balance in account", self.depositAmt)

    def deposit(self, amount):
        self.depositAmt += amount
        return self.depositAmt

    def buy_gift_subscription(self, other_user, year):
        print("Attempting gift subscription for", other_user)
        self._name=other_user
        self.subscribe(year)

    def get_subscription_price(self):
        return self._subscription_price

    def get_name(self):
        return self._name


obj = Problem13('vaishnavi', SUBSCRIPTION_PRICE)
obj.deposit(100)
obj.subscribe(2022)
obj.buy_gift_subscription('krishnapur', 2023)
