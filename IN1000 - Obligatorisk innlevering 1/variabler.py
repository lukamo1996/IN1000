## Oppgave 1: Utskrift og innlesing med variabler
## Jeg bruker F-string formattering nedenfor der variablene legges inn i {}

fornavn = input("Hva er fornavnet ditt?")
print (f"Hei {fornavn}")
alder = int(input("Hvor gammel er du?"))
årstall = int(input("Hvilket år befinner vi oss i nå?"))

print(alder)
print(årstall)

fødselsår = årstall - alder
print(f"Differanse: {fødselsår}")

etternavn = input("Hva er etternavnet ditt?")
sammen = f"{fornavn} {etternavn}"
print(sammen)

sammen = f"{fornavn} og {etternavn}"
print(sammen)