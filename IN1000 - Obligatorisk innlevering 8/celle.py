class Celle:
    #Konstruktør
    def __init__(self):
        self._status = "død"
        
    #Hent status
    def status(self):
        return self._status

    #Endre status
    def settDoed(self):
        self._status = "død"

    #Sett levende
    def settLevende(self):
        self._status = "levende"

    #Hent status
    def erLevende(self):
        if self.status() == "levende":
            return True
        else: return False
    
    #Status-symbol
    def statusTegn(self):
        if self.status() == "levende": return "O"
        elif self.status() == "død": return "."