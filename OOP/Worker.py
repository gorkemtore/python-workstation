class Worker():
    def __init__(self, _name, _salary, _department):
        print("Çalışan sınıfının init fonksiyonu.")
        self.name = _name
        self.salary = _salary
        self.department = _department

    def showInfo(self):
        print(self.name)
        print(self.salary)
        print(self.department)

    def changeDepartment(self, newDep):
        self.department = newDep