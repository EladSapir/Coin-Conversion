class Shekel(Coin):
    """
    shekel class - coin of New Israeli Shekel
    """

    def __str__(self):
        """
        converts to Shekel to string
        :return: format of Shekel
        """
        return f'{self.getQuantity()}ג‚×'

    def __repr__(self):
        """
        function returns a printable representation of Shekel
        :return: format of printable representation of Shekel
        """
        return f'Shekel({self.getQuantity()})'

    def __add__(self, other):
        """
        add between Shekel and other Shekel
        :param other: other Shekel
        :return: sum of two Shekels
        """
        if type(other) == Shekel:
            return self.getQuantity() + other.getQuantity()

    def __sub__(self, other):
        """
        sub between Shekel and other Shekel
        :param other: other Shekel
        :return: subtraction result of two Shekels
        """
        if type(other) == Shekel:
            return self.getQuantity() - other.getQuantity()

class Dollar(Coin):
    """
    Dollar class - coin of New Israeli Shekel
    """

    def amount(self):
        """
        converts to New israeli shekel
        :return: the conversion to NIS
        """
        return self.getQuantity() * rates['dollar', 'nis']

    def __str__(self):
        """
        converts to Dollar to string
        :return: format of Shekel
        """
        return f'{self.getQuantity()}$'

    def __repr__(self):
        """
        function returns a printable representation of Dollar
        :return: format of printable representation of Dollar
        """
        return f'Dollar({self.getQuantity()})'

class Euro(Coin):
    """
    Euro class - coin of New Israeli Shekel
    """

    def amount(self):
        """
        converts to New israeli shekel
        :return: the conversion to NIS
        """
        return self.getQuantity() * rates['euro', 'nis']

    def __str__(self):
        """
        converts to Euro to string
        :return: format of Shekel
        """

        return f'{self.getQuantity()}ג‚¬'

    def __repr__(self):
        """
        function returns a printable representation of Euro
        :return: format of printable representation of Euro
        """
        return f'Euro({self.getQuantity()})'


def add(x, y):
    """
    add bwtween two coins
    :param x: first coin
    :param y: second coin
    :return: sum of the coins
    """
    return x + y


def sub(x, y):
    """
    sub between two coins
    :param x: first coin
    :param y: second coin
    :return: Subtraction result
    """
    return x - y

def typeTag(x):
    """
    gets coin and returns format of its type
    :param x: given coin
    :return: format of the type of the coin
    """
    if type(x) == Shekel: return f'nis'
    if type(x) == Dollar: return f'dollar'
    if type(x) == Euro: return f'euro'


def addShekelWithAny(x, y):
    """
    gets two coins and returns the sum - first one must be shekel
    :param x: shekel coin
    :param y: second coin
    :return: sum of the coins
    """
    return f'Shekel({x.amount() + y.amount()})'


def subShekelWithAny(x, y):
    """
    gets two coins and returns the subtraction - first one must be shekel
    :param x: shekel coin
    :param y: second coin
    :return: sub of the coins
    """
    return f'Shekel({x.amount() - y.amount()})'


def addDE(x, y):
    """
    gets two coins and returns the sum - Dollar and Euro , using rates dictionary
    :param x: Dollar coin
    :param y: Euro coin
    :return: sum of the coins
    """
    return f'Dollar({x.getQuantity() + y.getQuantity() * rates["euro", "dollar"]})'


def addDS(x, y):
    """
    gets two coins and returns the sum - Dollar and Shekel , using rates dictionary
    :param x: Dollar coin
    :param y: Shekel coin
    :return: sum of the coins
    """
    return f'Dollar({x.getQuantity() + y.getQuantity() * rates["nis", "dollar"]})'


def addED(x, y):
    """
    gets two coins and returns the sum - Euro and Dollar , using rates dictionary
    :param x: Euro coin
    :param y: Dollar coin
    :return: sum of the coins
    """
    return f'Euro({x.getQuantity() + y.getQuantity() * rates["dollar", "euro"]})'


def addES(x, y):
    """
    gets two coins and returns the sum - Euro and Shekel , using rates dictionary
    :param x: Euro coin
    :param y: Shekel coin
    :return: sum of the coins
    """
    return f'Euro({x.getQuantity() + y.getQuantity() * rates["nis", "euro"]})'


def subDE(x, y):
    """
    gets two coins and returns the subtraction - Dollar and Euro , using rates dictionary
    :param x: Dollar coin
    :param y: Euro coin
    :return: sub of the coins
    """
    return f'Dollar({x.getQuantity() - y.getQuantity() * rates["euro", "dollar"]})'


def subDS(x, y):
    """
    gets two coins and returns the subtraction - Dollar and Shekel , using rates dictionary
    :param x: Dollar coin
    :param y: Shekel coin
    :return: sub of the coins
    """
    return f'Dollar({x.getQuantity() - y.getQuantity() * rates["nis", "dollar"]})'


def subED(x, y):
    """
    gets two coins and returns the subtraction - Euro and Dollar , using rates dictionary
    :param x: Euro coin
    :param y: Dollar coin
    :return: sub of the coins
    """
    return f'Euro({x.getQuantity() - y.getQuantity() * rates["dollar", "euro"]})'


def subES(x, y):
    """
    gets two coins and returns the subtraction - Euro and Shekel , using rates dictionary
    :param x: Euro coin
    :param y: Shekel coin
    :return: sub of the coins
    """
    return f'Euro({x.getQuantity() - y.getQuantity() * rates["nis", "euro"]})'


def apply(operation, x, y):
    """
    function that applies operation on two coins according to the dictionary
    :param operation: operation to apply
    :param x: first coin
    :param y: second coin
    :return: result of the operation between the coins
    """
    implementations = {('add', ('dollar', 'euro')): addDE,
                       ('add', ('dollar', 'nis')): addDS,
                       ('add', ('euro', 'dollar')): addED,
                       ('add', ('euro', 'nis')): addES,
                       ('add', ('nis', 'euro')): addShekelWithAny,
                       ('add', ('nis', 'dollar')): addShekelWithAny,
                       ('sub', ('dollar', 'euro')): subDE,
                       ('sub', ('dollar', 'nis')): subDS,
                       ('sub', ('euro', 'dollar')): subED,
                       ('sub', ('euro', 'nis')): subES,
                       ('sub', ('nis', 'euro')): subShekelWithAny,
                       ('sub', ('nis', 'dollar')): subShekelWithAny,
                       }
    tags = (typeTag(x), typeTag(y))
    key = (operation, tags)
    return implementations[key](x, y)


def coerce_apply(operation, x, y):
    """
    function that applies operation on two coins according to the dictionary of coersions to NIS
    :param operation: operation to apply
    :param x: first coin
    :param y: second coin
    :return: result of the operation between the coins
    """
    tx, ty = typeTag(x), typeTag(y)
    implementations = {('add', 'nis'): add, ('sub', 'nis'): sub}
    if type(x) != Shekel and type(y) != Shekel:
        x, y = coercions[(tx, 'nis')](x), coercions[(ty, 'nis')](y)
    if type(x) != Shekel and type(y) == Shekel:
        x = coercions[(tx, 'nis')](x)
    if type(y) != Shekel and type(x) == Shekel:
        y = coercions[(ty, 'nis')](y)
    return Shekel(implementations[operation, 'nis'](x, y))


def EtoNis(x):
    """
    Euro to Nis
    :param x: Euro coin
    :return: conversion of the Euro to Shekel
    """
    return Shekel(x.getQuantity() * rates[('euro', 'nis')])


def DtoNis(x):
    """
    Dollar to Nis
    :param x: Dollar coin
    :return: conversion to Nis
    """
    return Shekel(x.getQuantity() * rates['dollar', 'nis'])


rates = {('nis', 'dollar'): 1 / 3.82, ('nis', 'euro'): 1 / 4.07, ('dollar', 'nis'): 3.82,
         ('dollar', 'euro'): 4.07 / 3.82, ('euro', 'nis'): 4.07, ('euro', 'dollar'): 3.82 / 4.07}

coercions = {('dollar', 'nis'): DtoNis, ('euro', 'nis'): EtoNis}


# all the operations from the examples in the Exercise:


s = Shekel(50)
d = Dollar(50)
e = Euro(50)
print(d.amount())
print(e.amount())
print(d + s)
print(add(e, d))
z = eval(repr(d))
print(z)
print(s)
print(e)

print(apply('add', Shekel(50), Dollar(20)))
rates[('euro', 'dollar')] = 1.06
print(apply('add', Dollar(50), Euro(20)))
print(apply('sub', Dollar(50), Euro(20)))

print(coercions[('dollar', 'nis')](Dollar(50)))
print(coerce_apply('add', Shekel(50), Dollar(20)))
print(coerce_apply('add', Dollar(50), Euro(20)))
print(coerce_apply('sub', Dollar(50), Euro(20)))
