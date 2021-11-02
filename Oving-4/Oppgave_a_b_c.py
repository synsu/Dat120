def pris_billett(alder):

    if alder < 18:
        resultat = 20

    elif alder < 67:
        resultat = 40

    else:
        resultat = 20

    while alder < 0:
        resultat = input("ikke gyldig alder")
        break


    return resultat


for i in range(5):
    alder_til_kunde_streng = input("Alder i år: ")
    alder_til_kunde = int(alder_til_kunde_streng)
    pris = pris_billett(alder_til_kunde)

    print(pris)








