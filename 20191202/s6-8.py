class Person():
    def __init__(self, name):
        self.name = name

    def job(self):
        print("老師")


class EngineerPersion(Person):
    def __init__(self, name):
        self.name = name + "資深工程師"

    def job(self):
        print("工程師")


frank = Person("Pon Hsiao")
enginer = EngineerPersion("PonPon")
print(frank.name)
print(enginer.name)
frank.job()
enginer.job()
