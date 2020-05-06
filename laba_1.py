class myclass():
    def __init__(self, x):
        self.x = x
        
    def calc_1(self):
        try:
            if self.x <= 1.696 or self.x >= 61.802:
                return self.x ** 4 * 2.868 + self.x ** 3 * 3.429 - self.x ** 2 * 4.987 + self.x * 1.181
        except TypeError:
            return "Error"

    def calc_2(self):
        try:
            if self.x <= 1.696 or self.x >= 61.802:
                return self.x ** 3 * 3.791 - self.x ** 2 * 3.656 + self.x * 2.612
        except TypeError:
            return "Error"

    def calc_3(self):
        try:
            if self.x <= 1.696 or self.x >= 61.802:
                return self.x ** 2 * 2.152 + self.x * 4.383
        except TypeError:
            return "Error"

    def calc_4(self):
        try:
            if self.x <= 1.696 or self.x >= 61.802:
                return self.x * 9.825
        except TypeError:
            return "Error"

if __name__ == '__main__':
    x = float(input("input float: "))
    m = myclass(x)
    print(m.calc_1())
    print(m.calc_2())
    print(m.calc_3())
    print(m.calc_4())
