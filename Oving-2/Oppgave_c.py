def heltall(tall):

    if tall>0:
        return int(tall)
    else:
        return False

sum=0  #kode starter (det er dette vi skal finne i oppgaven)
while True:
    heltall_streng=input("positive heltall: ")
    heltall_int=heltall(int(heltall_streng)) #kaller på funksjonen
    if heltall_int:
        sum += heltall_int
        print(sum)
    else:
        break

print(sum)

















