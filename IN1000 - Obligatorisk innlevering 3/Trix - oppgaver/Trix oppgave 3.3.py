## Trix oppgave 3.1 - String-liste med måneder
def hvilkenMåned(tall):
    måneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
    if(tall < 1 or tall > 12): return "Det tallet er ikke en måned."
    else: return måneder[tall - 1]

print(hvilkenMåned(5))