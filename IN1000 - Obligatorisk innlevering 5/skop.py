## Oppgave 3: Skop
"""
1. Funksjonen minFunksjon() defineres.
2. Funksjonen hovedprogram() defineres.
3. hovedprogram() kjører:
    -> a = 42
    -> b = 0
    -> b = a (42)
    -> a = minFunksjon(), mens b fortsatt er lik 42.
4. minFunksjon() kjører:
    for loopen starter
        i = 0
            -> c = 2
            -> c = c + 1, c = 3
            -> b = 10
            -> b = b + a(a finnes ikke, så vi får en feilmelding)
            ...resten av kjøringen stopper opp. Grunnen til dette er at variabelen 'a' inni funksjonen hovedprogram er ikke tilgjengelig for funksjonen minFunksjon ettersom den ikke er i global-skop. Den er altså ikke tilgjengelig i "the global namespace". Det vil si at variabelen er ikke en egenskap til global-objektet, noe som gjør variabelen kun tilgjengelig i avgrensede områder (i vårt tilfellet bare innad funksjonene selv). Hvis vi hadde satt a-variabelen i funksjon hovedprogram til "global a", så hadde alt funket helt fint.
"""