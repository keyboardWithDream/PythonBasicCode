class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.Fish = Fish(y)

    def print_num(self):
        print("Pool里有%d只Turtle和%dFish" % (self.turtle.num, self.Fish.num))


pool = Pool(2, 10)
pool.print_num()
a = 12345
a <<= 2
print(a)