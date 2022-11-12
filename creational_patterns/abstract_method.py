from enum import Enum


class PizzaType(Enum):
    MARGARITA = 0,
    MEXICO = 1,
    DIABLO = 2


class Pizza:

    def __init__(self, price: float):
        self.__price = price

    @property
    def price(self):
        return self.__price


class PizzaMargarita(Pizza):

    def __init__(self):
        super().__init__(5.5)


class PizzaMexico(Pizza):

    def __init__(self):
        super().__init__(4.2)


class PizzaDiablo(Pizza):

    def __init__(self):
        super().__init__(6.9)


def create_pizza(pizza_type: PizzaType) -> Pizza:
    factory = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.DIABLO: PizzaDiablo
    }
    return factory[pizza_type]()


if __name__ == "__main__":
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f"Pizza type: {pizza}, pizza price: {my_pizza.price}")



