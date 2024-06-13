from decouple import config
import random


class Game:
    def __init__(self):
        self.range_start = config('RANGE_START', cast=int)
        self.range_end = config('RANGE_END', cast=int)
        self.attempts = config('ATTEMPTS', cast=int)
        self.capital = config('CAPITAL', cast=int)
        self.number = random.randint(self.range_start, self.range_end)

    def guess(self, bet, number):
        if number == self.number:
            self.capital += bet * 2
            return True
        else:
            self.capital -= bet
            return False
