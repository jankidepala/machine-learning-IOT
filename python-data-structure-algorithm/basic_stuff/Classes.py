class Animal:
    roar=""

    def __init__(self, name):
        self.name = name
        Animal.roar = "Y"

    def walk(self):
        print("Total Animal %d" % Animal.roar)


