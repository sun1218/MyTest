class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()

    def __iter__(self):
        return self


for n in Fab(10):
    print(n)

print("——————————————————————————————")


def Fab_2(max):
    n, a, b = 0, 0, 1

    while n < max:
        yield b
        temp = a + b
        a = b
        b = temp
        n += 1


for n in Fab_2(10):
    print(n)
