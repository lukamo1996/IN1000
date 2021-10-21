## Importerer Hund-klassen fra hund.py-filen
from hund import Hund

## Kjør program
def hovedProgram():
    hund = Hund(20, 13)
    hund.spring()
    hund.spis(13)
    print(hund.vekt())
    hund.spis(13)
    print(hund.vekt())

hovedProgram()
