## Vi importerer klassen fra motorsykkel.py-filen
from motorsykkel import Motorsykkel

def hovedProgram():
    sykkel1 = Motorsykkel("Harley Davidson", "1B23X9", 18314)
    sykkel2 = Motorsykkel("Vespa", "1JXXZY", 1931)
    sykkel3 = Motorsykkel("Tesla", "WYCCC3", 183)
    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()
    sykkel3.kjor(10)
    print(sykkel3.hentKilometerstand())

hovedProgram()
