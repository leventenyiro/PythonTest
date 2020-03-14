class Osztaly:
    def __init__(self, x):
        self.x = x

    def szorzas(self, y):
        return self.x * y

    #def getX(self):
    #    return self.x

o = Osztaly(5)
print(o.x)
s = o.szorzas(6)
print(str(s))