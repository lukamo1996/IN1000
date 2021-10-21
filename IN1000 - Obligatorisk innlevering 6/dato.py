## Oppgave 4: Dato
## 1) og 2)

class Dato():
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyttAar = nyttAar

    def år(self):
        return self._nyttAar

    def dato(self):
        return f"{self._nyDag}.{self._nyMaaned}.{self._nyttAar}"

    def lik(self, dato):
        return True if dato == self.dato() else False

    ## Denne metoden sjekker om datoen den kjører fra kommer
    ## før datoen den kjører fra e.g. kommerdenne.før(denne)
    def før(self, dato2):
        d1, m1, å1 = self.dato().split(".")
        d2, m2, å2 = dato2.split(".")
        if å1 < å2: return True
        elif å1 > å2: return False
        elif m1 < m2: return True
        elif m1 > m2: return False
        elif d1 < d2: return True
        elif d1 > d2: return False
        elif d1 == d2: return "Like"

    ## Metoden tar for seg spesialtilfellene:
    ## nyttår og overgang til ny måned. Skuddår er ikke inkludert.
    ## Tallene i tabellen viser til antallet dager i gitt mnd
    ## Første if-statement forteller oss om vi er i siste dag av mnd-en
    ## If-statement inni der igjen forteller oss om det er siste måned
    ## Hvis ikke bytt måned hvis ja, lag nytt år.
    def nesteDag(self):
        datoTabell = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        if datoTabell[self._nyMaaned] == self._nyDag:
            if self._nyMaaned == 12:
                self._nyDag = 1
                self._nyMaaned = 1
                self._nyttAar = self._nyttAar + 1
            else:
                self._nyDag = 1
                self._nyMaaned = self._nyMaaned + 1
        else:
            self._nyDag = self._nyDag + 1
