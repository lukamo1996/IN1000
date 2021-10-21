## Oppgave 1: Klassen sang

## __str__-metoden blir kallet på når man f.eks. prøver å printe ut det gitte Sang-objektet. Jeg bruker dette bare i spill()-metoden.
## sjekkTittel og sjekkArtistogTittel tar i bruk en tertiær operatør som kondenserer if/else-uttrykket.
## sjekkTittel-metoden returnerer True hvis tittelen som legges inn er lik tittel-verdien til det gitte objektet. Hvis ikke så returneres False.
## sjekkArtistOgTittel returnerer True hvis både artisten samsvarer med artisten og tittelen samsvarer med tittelen. Ellers returneres False.
## I sjekkArtist så ble det ikke påpekt i oppgaven om vi skal skille mellom små og store bokstaver. Jeg valgte å anse de som forskjellige. Queen er altså != queen.

class Sang:
    def __init__(self, artist, tittel):
        self._tittel = tittel
        self._artist = artist

    def __str__(self):
        return f"{self._tittel} av {self._artist}"

    def spill(self):
        print (f"Spiller {self}")

    def tittel(self):
        return self._tittel

    def artist(self):
        return self._artist

    def sjekkArtist(self, navn):
        for el in navn.split(" "):
            if el in self.artist().split(" "): return True
        return False

    def sjekkTittel(self, tittel):
        return True if tittel.lower() == self.tittel().lower() else False

    def sjekkArtistOgTittel(self, artist, tittel):
        return True if self.sjekkArtist(artist) and self.sjekkTittel(tittel) else False
