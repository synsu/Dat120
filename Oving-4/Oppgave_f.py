import math

def eclidske_avstand(x, y):
    avstand = math.sqrt(x**2+y**2) #formelen til avstand mellom to punkt
    return avstand

if __name__ == '__main__': #main- kjører bare i denne filen
    x = int(input("x-verdi til punkt: "))
    y = int(input("y-verdi til punkt: "))

    avstand = eclidske_avstand(x, y)

    print(avstand)
