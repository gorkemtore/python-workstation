class Animal():
    def __init__(self, type, age, color):
        self.type = type
        self.age = age
        self.color = color
        self.isHungry = True
    def eat(self):
        if(self.isHungry):
            print("The animal is eating food.")
            self.isHungry = False
        else:
            print("The animal does not hungry!")
            #yemek yemeyi reddettikten sonra acıktı.
            self.isHungry = True