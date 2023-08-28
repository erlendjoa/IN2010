

nrOfSeeds = int(input())
growthTimesInput = input().split(" ")
growthTimes = sorted(growthTimesInput, reverse=True)


class Seed:
    def __init__(self, n):
        self.n = n
    def grow(self):
        self.n -= 1
        if self.n == 0:
            self = None

f