import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class Abstract_pizza_maker(object):

    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.15 * self.get_cost()


class Concrete_pizza_maker(Abstract_pizza_maker):

    def get_cost(self):
        return 10.0

    def get_ingredients(self):
        return 'pizza'


@six.add_metaclass(ABCMeta)
class Abstract_pizza_maker_Decorator(Abstract_pizza_maker):

    def __init__(self, decorated_pizza):
        self.decorated_pizza = decorated_pizza

    def get_cost(self):
        return self.decorated_pizza.get_cost()

    def get_ingredients(self):
        return self.decorated_pizza.get_ingredients()


class Massa(Abstract_pizza_maker_Decorator):

    def __init__(self, decorated_pizza):
        Abstract_pizza_maker_Decorator.__init__(self, decorated_pizza)

    def get_cost(self):
        return self.decorated_pizza.get_cost()

    def get_ingredients(self):
        return self.decorated_pizza.get_ingredients() + ', Massa'


class Molho(Abstract_pizza_maker_Decorator):

    def __init__(self, decorated_pizza):
        Abstract_pizza_maker_Decorator.__init__(self, decorated_pizza)

    def get_cost(self):
        return self.decorated_pizza.get_cost() + 7.5

    def get_ingredients(self):
        return self.decorated_pizza.get_ingredients() + ', molho'


class Queijo(Abstract_pizza_maker_Decorator):

    def __init__(self, decorated_pizza):
        Abstract_pizza_maker_Decorator.__init__(self, decorated_pizza)

    def get_cost(self):
        return self.decorated_pizza.get_cost() + 5.0

    def get_ingredients(self):
        return self.decorated_pizza.get_ingredients() + ', queijo'

