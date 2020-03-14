class Osztaly:
    x = 5
    def ketszerezes(self):
        return self.x * 2

osztaly = Osztaly()
print(osztaly.x)
x = osztaly.ketszerezes()
print("Kétszer: " + str(x))