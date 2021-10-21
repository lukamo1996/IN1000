## Oppgave 2: Temperatur
ordbok = {}

## Her åpner vi opp .csv filen og splitter den med \n som separator. Deretter slicer vi den og fjerner det siste tallet ettersom dette er bare en tom-string. Så looper vi over stringen og for hver strin så splitter vi den med komma som separator og setter måneden lik temperaturen. 
def mndToDict(fil):
    fil = open(fil, "r").read()
    fil = fil.split("\n")[0:-1]
    for el in fil:
        el = el.split(",")
        ordbok[el[0]] = el[1]
    print(ordbok)

mndToDict("max_temperatures_per_month.csv")

## Vi åpner opp filen, splitter og fjerner siste tomme string ''. Deretter looper vi over alle elementene i string-filen og sjekker om den gitte verdien til den gitte månedene har en verdi som er lavere enn den gitte dagen som loopes over. Hvis den er mindre så fant vi en ny rekord. Dette printes ut og vi setter den nye verdien til den gamle verdien.
def tempToDict(ordbok, fil):
    fil = open(fil, "r").read()
    fil = fil.split("\n")[0:-1]
    for el in fil:
        el = el.split(",")
        if float(ordbok[el[0]]) < float(el[2]):
            print(f"Vi fant en ny rekord for måneden {el[0]} med en ny temp på {el[2]} celsius fra den tidligere {ordbok[el[0]]} celsius. Dæven steike!")
            ordbok[el[0]] = float(el[2])
    return ordbok

tempToDict(ordbok, "max_daily_temperature_2018.csv")

## Skriv inn ordboken i en .csv fil.
def saveToFile(ordbok, filnavn):
    fil = open(filnavn, "w")
    for el in ordbok: fil.write(f"{el},{ordbok[el]}\n")
    print(fil)

saveToFile(ordbok, "max_temperatures_per_month.csv")

## Ekstraoppgave
## Åpne filen, les den, split den, fjern siste tomme streng. Vi sette count lik 0.
## Vi lager en loop som er lik lengden til den splittede filen også sjekker vi om temperaturen på den gitte dagen er høyere enn 25 celsius. Hvis den er det så setter inkrementerer vi count med +1. 
## Hvis den ikke er det så betyr det at vi går ut av "streaken" vår. Da sjekker vi om count er større enn eller lik 5. Hvis den er det så finner ut når varmebølgen begynte og når den ble avsluttet. Dette printer vi ut og setter count tilbake til 0. Hvis count ikke er større eller lik 5 så er vi fortsatt ute av streaken vår og da setter vi count igjen lik 0.
def varmeBølge(fil):
    fil = open(fil, "r").read()
    fil = fil.split("\n")[0:-1]
    count = 0
    for i in range(0, len(fil), 1):
        if float(fil[i].split(",")[2]) > 25: 
            count = count + 1
        else:
            if count >= 5:
                start = fil[i - count].split(",")
                slutt = fil[i].split(",")
                print(f"Vi fant en varmebølgen. Varmebølgen begynte {start[1]}.{start[0]} og endte {slutt[1]}.{slutt[0]}")
                count = 0
            else: count = 0

varmeBølge("max_daily_temperature_2018.csv")