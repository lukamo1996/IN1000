import random
from celle import Celle

class Spillebrett:
    #Konstruktør
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._genNummer = 0
        self._opprettBrett()
        self._generer()
    
    #Rader
    def rader(self):
        return self._rader
    
    #Kolonner
    def kolonner(self):
        return self._kolonner

    #Generasjonsnummer
    def generasjon(self):
        return self._genNummer

    #Rutenettet
    def rutenett(self):
        return self._rutenett

    #Print nåværende rutenett med ledsagende generasjonsinfo. Temp-listen har som funksjon å være et lagringssted for status-symbolene fra listene som loopes over.
    def tegnBrett(self):
        for el in self.rutenett():
            temp = []
            for el2 in el: 
                temp.append(el2.statusTegn())
            print(" ".join(temp))
        print(f"Generasjon {self.generasjon()} - Antall levende celler: {self.finnAntallLevende()}")

    #Seed spillbrettet. Vi looper over alle cellene og gir cellen en levende|død-status basert på random.randInt-verdien.
    #30% sannsynlig for at en celle får statusen "levende" 
    def _generer(self,):
        for el in self.rutenett():
            for el2 in el:
                num = random.randint(0,3)
                if num < 1: el2.settLevende()
                else: el2.settDoed()

    #Vi lager et spillbrett basert på antall rader og kolonner brukeren ønsker.
    #Først fyller vi opp hver hver indre liste (raden) med rad-antall celler og deretter pusher vi listen inn i en temp-liste
    #...som så pushes inn i selve rutenett-listen
    def _opprettBrett(self):
        for i in range(self.rader()):
            arr = []
            for j in range(self.kolonner()): 
                arr.append(Celle())
            self._rutenett.append(arr)

    #Vi looper over rader-listene som vi så looper over igjen. Hver celle innad rader-listen passes til finnNabo funksjonen som finner antallet naboer
    #Deretter finner vi ut antallet celler som er levende.
    #Antallet med levende-celler finner vi ved å finne lengden på listen med levende celler i list-comprehensionen.
    #Det som ledsager i if-statementene er spillets regler.
    #Vi ønsker å oppdatere alle cellene sammen i en kontinuerlig endring og ikke underveis - ettersom dette vil føre til at verdiene endres mens vi looper
    #Vi endrer disse verdiene i 2 list-comprehensions på slutten. Her setter vi alle cellene i skalDø og skalLeve til henholdsvis død og levende
    def oppdatering(self):
        self._genNummer = self._genNummer + 1
        rutenett = self.rutenett()
        skalLeve = []
        skalDø = []
        for x in range(self.rader()):
            for y in range(self.kolonner()):
                celle = rutenett[x][y]
                naboer = self.finnNabo(x, y)
                levende = len([el for el in naboer if el.erLevende()])
                if celle.erLevende():
                    if levende < 2: skalDø.append(celle)
                    elif levende > 3: skalDø.append(celle)
                elif celle.erLevende() == False:
                    if levende == 3: skalLeve.append(celle)
        [el.settDoed() for el in skalDø]
        [el.settLevende() for el in skalLeve]

    #Loop over alle cellene i rutenettet og sjekk om cellen lever. Returner antallet levende
    def finnAntallLevende(self):
        count = 0
        for liste in self.rutenett(): 
            for celle in liste: 
                if celle.erLevende(): count = count + 1
        return count

    #Funksjonen tar imot x og y verdien fra en celle. Deretter looper den over koordinatene i koordinater-listen.
    #x og y-verdiene cellen sendt fra oppdatering() blir addert med tilsvarende verdier i koordinater listen. 
    #Til slutt prøver vi å pushe den gitte cellen inn i arr i et try-uttrykk. Hvis det går, flott, hvis ikke (f.eks. høyere indeks) catch og pass.
    #If statementen er for å hindre at negative indekser blir gjort om til python slice-uttrykk.
    #Til slutt returnerer vi antallet naboer som finnes.
    def finnNabo(self, rad, kolonne):
        arr = []
        koordinater = [
            [-1, -1],
            [0, -1],
            [1, -1],
            [-1, 0],
            [1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
        ]
        for el in koordinater:
            rutenett = self.rutenett()
            x, y = el
            x = rad + x
            y = kolonne + y
            if x >= 0 and y >= 0:
                try: arr.append(rutenett[x][y])
                except: pass
        return arr