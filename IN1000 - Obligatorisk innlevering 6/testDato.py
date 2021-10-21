## 3)
## Importer Dato-klassen fra dato.py-filen
from dato import Dato

## Lag et objekt med Dato-klassen
## Måned-tabellen forteller oss kobler mnd-tall til mnd-streng
def program():
    månedTabell = {
        "1": "januar",
        "2": "februar",
        "3": "mars",
        "4": "april",
        "5": "mai",
        "6": "juni",
        "7": "juli",
        "8": "august",
        "9": "september",
        "10": "oktober",
        "11": "november",
        "12": "desember",
    }
    dato = Dato(15, 2, 1996)
    dag, måned, år = dato.dato().split(".")
    print(dato.år())

    if dag == "15":
        print("Loenningsdag!")
    elif dag == "1":
        print("Ny maaned, nye muligheter")

    ## Skriv ut dato i lesbar-form
    streng = f"{dag}. {månedTabell[måned]} {år}"
    print(streng)

    dato.nesteDag()
    print(dato.dato())

    ## *-operatoren åpner opp listen og sender de inn som argumenter
    nyDato = Dato(*input("Skriv inn en dato i følgende format 15.2.2020: ").split("."))
    if nyDato.før(dato.dato()) == True:
        print("Den nye datoen kommer før den første datoen")
    elif nyDato.før(dato.dato()) == False:
        print("Den nye datoen kommer etter den første datoen")
    else:
        print("Den nye datoen og den første datoen er samme dag.")

program()
