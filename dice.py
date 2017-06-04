import random


class Die:
    # constructor
    def __init__(self, sides=2, value=0):
        # can't have a 1 sided die...
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        # can't have letters either...
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        # if all is well, give back a random value within the
        # number of sides on the die
        self.value = value or random.randint(1, sides)

    # turn an instance of the Die into an integer
    def __int__(self):
        return self.value

    # equality, allow comparing die value to other values.
    # Ie. Die() instance is less than 4, etc.

    # equal to
    def __eq__(self, other):
        return int(self) == other

    # not equal to
    def __ne__(self, other):
        return int(self) != other

    # greater than
    def __gt__(self, other):
        return int(self) > other

    # less than
    def __lt__(self, other):
        return int(self) < other

    # greater than or equal to
    def __ge__(self, other):
        return int(self) > other or int(self) == other

    # less than or equal to
    def __le__(self, other):
        return int(self) < other or int(self) == other

    # allow adding 2 dice to one another
    def __add__(self, other):
        return int(self) + other

    # radd = right hand operation
    def __radd__(self, other):
        return int(self) + other


class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
