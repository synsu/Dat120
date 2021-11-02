import Oppgave_f # siden oppgaven sier vi skal bruke samme funksjon

def avstand_mellom_to_punkt(punkt1, punkt2): #  punkt1 = (x, y)
    avstand = Oppgave_f.eclidske_avstand(punkt2[0]-punkt1[0], punkt2[1]-punkt1[1])# (x2-x1, y2-y1)
     #tuple- flere variabler i en variabel
     #brukt tuple her siden jeg har både en x og y verdi,
    return avstand


if __name__ == '__main__': #main- kjører bare i denne filen
    x1 = int(input("x-verdi til punkt1: "))
    y1 = int(input("y-verdi til punkt1: "))
    x2 = int(input("x-verdi til punkt2: "))
    y2 = int(input("y-verdi til punkt2: "))

    avstand = avstand_mellom_to_punkt((x1, y1), (x2, y2))

    print(avstand)
