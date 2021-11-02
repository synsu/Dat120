def billett(alder):
    if alder<18:
        resultat=20
    elif alder<67:
        resultat=40
    else:
        resultat=20
    return resultat


for i in range(5):
    alder_til_kunde_streng=input("Alder til kunde: ")
    alder_til_kunde=int(alder_til_kunde_streng)
    pris = billett(alder_til_kunde)

    print(pris)












