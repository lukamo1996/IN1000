## Oppgave 2: Beslutninger
valg = str(input("Har du lyst på brus?"))

## For å unngå å måtte skille mellom "Ja"/"ja"/"Nei"/"nei" så setter vi bare "ønske" til små bokstaver
if(valg.lower() == "ja"): print("Her har du en brus!")
elif(valg.lower() == "nei"): print("Den er grei.")
else: print("Det forstod jeg ikke helt.")