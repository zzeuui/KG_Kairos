class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def play(self):
        print('play')

p1 = Human("qwer", 11, "f")
p2 = Human("asdf", 22, "m")
print(p1.name)
print(p2.name)
p1.play()
