## Trix Oppgave: 2.8: Kroppstemperatur
kroppstemperatur = float(input("Hva er temperaturen din?"))
if(kroppstemperatur < 36.5): print("Du har hypotermi")
elif(kroppstemperatur > 37.5): print("Du har feber")
else: print("Du er frisk!")