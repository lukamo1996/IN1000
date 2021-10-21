## Trix oppgave 5.01 og 5.02
def forekommer(setning, bokstav):
    if bokstav in setning: return True

def utenRep(str): return "".join(set(str))

def antallUnike(str): return len(list(set(str)))