from abc import ABCMeta, abstractmethod


class Coke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self, hello):
        pass


class Coca(Coke):
    def drink(self, hello):
        print('drink Coca-Cola-' + hello)


class Pepsi(Coke):
    def drink(self, hello):
        print('drink Pepsi-Cola-' + hello)


class FastFoodRestaurant:
    @staticmethod
    def make_coke(name):
        return eval(name)()


if __name__ == '__main__':
    KCD = FastFoodRestaurant.make_coke('Coca')
    KCD.drink('hello')
