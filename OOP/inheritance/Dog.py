from Animal import Animal
class Dog(Animal):
    def __init__(self, type, age, color, speed):
        super().__init__(type, age, color)     
        self.speed = speed

        self.isRunning = False

    def run(self):
        if(self.isRunning == False):

            print("Running!!!")
            self.speed += 15
            self.isRunning = True

        else:
            print("Run method already worked.")

    def walk(self):
        if(self.isRunning):
            self.speed -= 15
            print("Walking...")
            self.isRunning = False
        
        else:
            print("The dog is walking.")