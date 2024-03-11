class Computer():
   
    def __init__(self, processor, threads, ghz):
        self.processor = processor
        self.threads = threads
        self.ghz = ghz
    
    #getter
    def getProcessor(self):
        return self.processor
    
    #setter
    def setProcessor(self, newProcessor):
        self.processor = newProcessor

    def getThreads(self):
        return self.threads
    def setThreads(self, newThreads):
        self.threads = newThreads
    
    def getGhz(self):
        return self.ghz
    def setGhz(self, newGhz):
        self.ghz = newGhz


    
    

        

