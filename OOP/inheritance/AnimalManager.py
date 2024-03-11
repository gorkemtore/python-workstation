"""

Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.

"""
from Animal import Animal
from Dog import Dog
from Bird import Bird


dog1 = Dog("Golden", 5, "Skin", 15)
print(dog1.speed)
dog1.run()
dog1.run()
dog1.walk()
dog1.walk()
dog1.eat()
dog1.eat()

print("--------------------------------------------")

bird1 = Bird("Eagle", 2, "Black", "Brown")
bird1.eat()
bird1.fly()