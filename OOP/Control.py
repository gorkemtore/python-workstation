from Developer import Developer
from Worker import Worker
from Admin import Admin
from Book import Book
from kumanda_sınıfı import Kumanda
from Computer import Computer

devoloper1 = Developer("Görkem" ,"Töre", 12345, 20000, ["Java", "Python", "C#"])
devoloper1.showInfo()

print()
devoloper1.increaseSalary(3000)
print(devoloper1.salary)

print("---------------------------")

worker1 = Admin("Ahmet", 500, "IT")
worker1.showInfo()
worker1.changeDepartment("Technician")
print("---------------------------")
worker1.showInfo()
print("**************************")




book = Book("İstanbul Hatırası", "Ahmet Ümit", 561, "Polisiye")
print(book)

print("------------------------")
"""
kumanda = Kumanda()
kumanda.rastgele_kanal()
print(kumanda)

"""


kumanda = Kumanda()

print("""

      1. Tv Aç
      2. Tv Kapat
      3. Ses Ayarları
      4. Kanal Ekle
      5. Kanal Sayısını Öğren
      6. Rastgele Kanala Geç
      7. Televizyon Bilgileri
      
      Press 'q' to exit. 

      """)


while False: #true yaparsan çalışır.

    islem = input("İslem seciniz: ")

    if(islem == "q"):
        print("İslem sonlandırılıyor")
        break
    
    elif(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()
    elif(islem == "3"):
        kumanda.ses_ayarlari()
    elif(islem == "4"):
        kanal = input("Kanal adı giriniz: ")
        kumanda.kanal_ekle(kanal)
    elif(islem == "5"):
        print("Kanal sayısı: ",len(kumanda))
    elif(islem == "6"):
        kumanda.rastgele_kanal()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem")


computer = Computer(processor="xeon e5450", threads=4, ghz=3.10)
print(f"Ghz: {computer.getGhz()}")
computer.setGhz(4.20)
print(f"Ghz: {computer.getGhz()}")
