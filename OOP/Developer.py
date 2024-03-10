class Developer():
    def __init__(self, name, surname, number, salary, languages):
        self.name = name
        self.surname = surname
        self.number = number
        self.salary = salary
        self.languages = languages

    def showInfo(self):
        print(f"İsim: {self.name}\nSoyisim:{self.surname}\nNumara:{self.number}\nMaaş:{self.salary}\nDiller:{self.languages}")

    def increaseSalary(self, amount):
        print("Zam yapılıyor")

        self.salary += amount
        print("Yeni maaş: ", self.salary)


        