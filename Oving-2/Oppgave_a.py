def sjekk_hoyde():
    lengde_meter_streng=input("lengde av person i cm: ")
    lengde_meter=float(lengde_meter_streng)
    if lengde_meter<120:
        resultat = "kan ikke ta"
    else:
        resultat = "kan ta"
    return resultat


for i in range(3):
    resultat = sjekk_hoyde()
    print(resultat)














