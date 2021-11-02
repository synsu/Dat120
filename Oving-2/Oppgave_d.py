def heltall(tall):

    if tall>0:
        return int(tall)
    else:
        return False

sum=0 #kode starter
antall=0 #antall/sum (gjennomsnitt) er det oppgaven sier vi skal finne
while True:
    heltall_streng=input("positive heltall: ")
    heltall_int=heltall(int(heltall_streng)) #kaller på funksjonen
    if heltall_int:
        sum += heltall_int
        antall += 1
        print(sum)
        print(sum/antall)
    else:
        break

print(sum/antall)

