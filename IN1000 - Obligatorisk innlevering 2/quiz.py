## Oppgave 5: Egen oppgave
## Lag et quiz-program med temaet "hovedstader" som stiller brukeren 5 spørsmål. Hver gang brukeren får riktig svar adderes ett poeng til en variabelpoengsum. Når brukeren har svart på alle de 5 spørsmålene så må brukeren få tilbakemelding på hvordan de presterte. Hvis brukeren svarer riktig på et spørsmål så må brukeren få an adekvat respons på dette, og det samme hvis de svarer feil. Hvis brukeren svarer riktig på alt så må de bli gratulert, hvis ikke, så får de ikke en gratulasjon.

## Selve quiz prosedyren/funksjonen
## Vi looper over spm-ordboken og stiller brukereren quizspørsmål. Hvis svaret er riktig, får de ett poeng og beskjed om det, hvis det er feil så får de også beskjed om det. Siste return-statement forteller brukeren hvordan de presterte og endrer tilbakemeldingen basert på poengsummen de fikk (ternary statement)
def quizMeg():
    ## Her har vi et objekt med noen spm og svar.
    spmer = {
        "1": {
            "spm": "Hva er hovedstaden i Norge?",
            "svar": "oslo"
        },
        "2": {
            "spm": "Hva er hovedstaden i Serbia?",
            "svar": "beograd"
        },
        "3": {
            "spm": "Hva er hovedstaden i Somalia?",
            "svar": "mogadishu"
        },
        "4": {
            "spm": "Hva er hovedstaden i Sverige?",
            "svar": "stockholm"
        },
        "5": {
            "spm": "Hva er hovedstaden i Montenegro?",
            "svar": "podgorica"
        },
    }
    poengsum = 0
    for s in spmer:
        svar = input(f"{spmer[s]['spm']} ").lower().strip()
        if svar == spmer[s]["svar"]:
            poengsum += 1
            print("Riktig svar!")
        else: print ("Feil :(")
    return f"Du fikk: {poengsum} av {len(spmer)} riktig! {'Gratulerer!' if poengsum > 4 else 'Prøv igjen :)'}"

print(quizMeg())
