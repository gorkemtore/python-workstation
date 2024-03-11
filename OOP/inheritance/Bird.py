from Animal import Animal

class Bird(Animal):
    def __init__(self, type, age, color, plumageColor):
        super().__init__(type, age, color)
        self.plumageColor = plumageColor

    def fly(self):
        print("Flying...")

    