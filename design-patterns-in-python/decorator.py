# @see http://ja.wikipedia.org/wiki/Decorator_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3

# Component and ConcreteComponent
class Price:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

# ConcreteDecorator
class WholesalePrice(Price):
    def __init__(self, price, advantage):
        self.price = price
        self.advantage = advantage
        Price.__init__(self, price.get_value())

    def get_value(self):
        return self.value + self.advantage

class DoublePrice(Price):
    def __init__(self, price):
        self.price = price
        Price.__init__(self, price.get_value())

    def get_value(self):
        return self.value * 2


if __name__ == '__main__':
    price = Price(1000)
    print price.get_value()
    print WholesalePrice(price, 20).get_value()
    print DoublePrice(price).get_value()
