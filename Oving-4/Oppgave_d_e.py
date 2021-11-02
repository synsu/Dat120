import math

def kinetisk_energi(masse, fart):    #komma- siden det skal være to variabler i funksjon
    energi = (masse*(fart**2))/2 #sett inn formel til kinetisk energi
    return energi


masse_streng = input("Masse til objekt: ")
masse = int(masse_streng)
fart_streng = input("Fart til objekt: ")
fart = int(fart_streng)


energi = kinetisk_energi(masse, fart)


print(energi)


