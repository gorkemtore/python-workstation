from Worker import Worker

class Admin(Worker):
    def getARaise(self, amount):
        self.salary += amount
