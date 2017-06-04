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


# Extend Hand to simulate a Yatzy specific die roll
class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        # Init with  5 six sided die
        super().__init__(size=5, die_class=D6, *args, **kwargs)

