## Trix 4.5 - Noen telle-funksjoner
def antallSifre(num):
    num = list(str(num))
    return len(num)
print(antallSifre(1023))

def antallBokstaver(str):
    return str.count("l")
print(antallBokstaver("Luka er lite loka i lillehammer"))

def strLengeHøyereEnnTallet(str, tall):
    if len(str) > tall:
        return True
    else: return False
print(strLengeHøyereEnnTallet("luka", 5))