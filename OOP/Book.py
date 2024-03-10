class Book():
    
    def __init__(self, name, writer, pageCount, category):
        print("init fonksiyonu")
        self.name = name
        self.writer =writer
        self.pageCount = pageCount
        self.category = category
    
    def __str__(self):
        return f"İsim: {self.name}\nWriter: {self.writer}\nKategori: {self.category}"