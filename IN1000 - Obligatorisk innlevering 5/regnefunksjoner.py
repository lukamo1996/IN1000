## Oppgave 1: Regnefunksjoner
## 1)
## Funksjonen erLovlig sjekker at alle argumentene, altså locals() er True og at alle tallene er int/float. Hvis disse betingelsene er tilfredsstilt så returneres True.
## Funksjonen tallFormatør tar tallene fra matte-funksjonene og gjør tallet om til en int- eller en float-verdi avhengig av om summen er et heltall eller ikke.
## locals() kan ikke brukes direkte så vi må legge argumentene i en args-variabel. Vi vet at dette blir en ordbok der alle argumentene er i en nøkkel som jeg har kalt 'a'. 
## Da bruker vi all()-metoden for å sjekke at alle argumentene er True og vi sjekker at alle verdiene i 'a' er enten heltall eller float vha. list-comprehensions og isinstance.
def erLovlig(a):
    args = locals()
    if all(args["a"]) and all(isinstance(args["a"][el], (int, float)) for el in args): return True

## Tallformatøren tar inn tallet og endrer det basert på om float-verdien er en int eller ikke. Hvis floaten er en int så gjør du det om til en int, hvis ikke, så bare runder du av til 2-desimaler.
def tallFormatør(a):
    if float(a).is_integer() == True: return int(a)
    else: return round(a, 2)

## Matte-funksjonene: Først sjekker vi om de oppgitte verdiene er tillatt og deretter returnerer vi verdien til funksjonen som kalte på den. Hvis ikke returnerer vi en passende beskjed.
def addisjon(a, b):
    if erLovlig(locals()) == True: return tallFormatør(a + b)
    else: return "Det der funker ikke."
def subtraksjon(a, b):
    if erLovlig(locals()) == True: return tallFormatør(a - b)
    else: return "Det der funker ikke."
def divisjon(a, b):
    if erLovlig(locals()) == True: return tallFormatør(a / b)
    else: return "Det der funker ikke."

## 2) 
assert(addisjon(1, 2) == 3)
assert(addisjon(1, -1) == 0)
assert(addisjon(-1, -1) == -2)
assert(subtraksjon(1, 2) == -1)
assert(subtraksjon(1, -1) == 2)
assert(subtraksjon(-2, -2) == 0)
assert(divisjon(1, 1) == 1)
assert(divisjon(-1, 1) == -1)
assert(divisjon(-1, -2) == 0.5)

## 3)
def tommerTilCm(antallTommer):
    assert antallTommer >= 0
    return antallTommer * 2.54
print(tommerTilCm(7))

## 4)
## Vi bruker list-comprehensions og gjør alle elementene inni input.split()-listen om til en float-verdi og deretter sender vi listen til argumenter-variabelen.
## Deretter går vi igjennom listen på nytt og gjør float verdiene som egentlig er heltall til heltall og lar de som ikke er det forbli float-verdier. Den eneste hensikten med denne denne biten er å gjøre verdiene mer representable for print-statementen etterpå. Vi ønsker at når vi printer ut f.eks. "20 minus 19 er lik = 1" så blir ikke 20 og 19 f.eks. skrevet ut som 20.0 og 19.0, vi kunne i prinsippet fjernet den biten.
def skrivBeregninrger():
    argumenter = [float(el) for el in input("Skriv inn to tall i dette formatet: 2 og 8: ").split(" og ")]
    argumenter = list(map(lambda x: int(x) if x.is_integer() else x, argumenter))
    print(f"{argumenter[0]} pluss {argumenter[1]} er lik = {addisjon(argumenter[0], argumenter[1])}")
    print(f"{argumenter[0]} minus {argumenter[1]} er lik = {subtraksjon(argumenter[0], argumenter[1])}")
    print(f"{argumenter[0]} delt på {argumenter[1]} er lik = {divisjon(argumenter[0], argumenter[1])}")
    print("Konvertering fra tommer til cm:")
    print(tommerTilCm(float(input("Skriv inn et tommertall som du vil ha til cm: "))))

skrivBeregninrger()