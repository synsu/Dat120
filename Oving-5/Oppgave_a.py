def sjekk_hoyde(hoyde):
    loop=True
    resultat=""
    while loop:
        try:
            lengde_meter=float(hoyde)
            if 0<=lengde_meter<120:
                resultat = "kan ikke ta"
                loop= False
            else:
                if lengde_meter >= 0:
                    resultat = "kan ta"
                    loop = False
                else:
                    print("negative tall er ikke lov")
                    hoyde=input("lengde av person i cm: ")
        except ValueError: #unntak
            print("ikke godkjent, prøv igjen")
            hoyde=input("lengde av person i cm: ")
    return resultat


test = input("lengde av person i cm")
print(sjekk_hoyde(test))



