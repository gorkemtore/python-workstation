import random
import time

class Kumanda():
    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["Trt","Atv","Fox","Star"], kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    
    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi azalt: '<' \nSesi artır: '>' \nÇıkış: 'çıkış' --->   ")

            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses : ",self.tv_ses)

            elif(cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses +=1
                    print("Ses:",self.tv_ses)

            else: 
                print("Ses Güncellendi: ",self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi.")


    def rastgele_kanal(self):
        self.kanal = random.choice(self.kanal_listesi)
        print("Mevcut kanal: ",self.kanal)

    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return f"Tv Durumu: {self.tv_durum}, \nTv Ses: {self.tv_ses}, \nKanal Listesi: {self.kanal_listesi}, \nŞu anki kanal: {self.kanal}"