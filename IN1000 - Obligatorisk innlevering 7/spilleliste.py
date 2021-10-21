## Oppgave 2: Klassen spilleliste

from sang import Sang

## Spilleliste-klassen
class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        filnavn = open(filnavn, "r")
        for el in filnavn:
            tittel, artist = el.strip().split(";")
            self._sanger.append(Sang(artist, tittel))
        filnavn.close()

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for el in self._sanger:
            el.spill()

    ## Loop over sangene og sjekk om tittelen satt inn finnes i gitt sang, hvis ja, returner den første sangen. Hvis ikke, returner None.
    def finnSang(self, tittel):
        for el in self._sanger:
            if el.sjekkTittel(tittel): return el
        return None

    ## Loop over sangene og sjekk om artistnavnet satt inn finnes i hver gitt sang. Hvis ja, push inn i listen, hvis ikke, gå videre. Returner listen til slutt.
    def hentArtistUtvalg(self, artistnavn):
        resultat = []
        for el in self._sanger:
            if el.sjekkArtist(artistnavn): resultat.append(el)
        return resultat
