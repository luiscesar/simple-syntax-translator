

class Switcher:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def call(self, case_x):
        switch = {
            1: lambda y: {
                print("x1 = " + str(self) + ", y1 = " + str(y))
            },
            2: lambda y: {
                print("x2 = " + str(self) + ", y2 = " + str(y))
            },
            3: self.case3
        }
        switch.get(case_x, lambda y: print("Default"))(case_x)

    def case3(self, y):
        self.name = "case3"
        print("x3 = " + str(self) + ", y3 = " + str(y))


