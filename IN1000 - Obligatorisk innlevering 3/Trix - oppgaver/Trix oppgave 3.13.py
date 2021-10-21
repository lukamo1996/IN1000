## Trix oppgave 3.13 - Ordbok med flaggfarger
flaggOrdbok = {
    "norge" : ["rødt", "hvitt", "blått"],
    "sverige" : ["blått", "gult"],
    "danmark" : ["rødt", "hvitt"],
    "finland" : ["hvitt", "blått"],
    "japan" : ["rødt", "hvitt"],
    "gabon" : ["grønt", "gult", "blått"],
    "storbritannia" : ["rødt", "blått", "hvitt"],
    "chile" : ["blått", "hvitt", "rødt"]
}

print(flaggOrdbok)
flaggOrdbok["serbia"] = ["blått", "rødt", "hvitt"]

def hvilkeFarger():
    farge = input("Skriv inn et land: ")
    if farge in flaggOrdbok: return flaggOrdbok[farge]
    else: return "Det landet finnes ikke i vår database"

print(hvilkeFarger())