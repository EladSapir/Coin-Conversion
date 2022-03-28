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
