from dice import D6


# Simulate a die roll
class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        # for whatever in size
        # (_ is a throwaway var, see https://stackoverflow.com/a/5893946 )
        for _ in range(size):
            self.append(die_class())
        # sort dice in hand
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
            return dice


# Extend Hand to simulate a Yatzy specific die roll
class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        # Init with  5 six sided die
        super().__init__(size=5, die_class=D6, *args, **kwargs)

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes),
        }
