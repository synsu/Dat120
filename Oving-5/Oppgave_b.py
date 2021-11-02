def mail_fra_fil(fil):
    with open(fil, "r") as f: #bruker with, så slipper å close
        liste = []
        for linje in f:
            if linje.find("From:") == 0: # Sjekker om "from" er første index i linjen
                fra = linje.find("<")
                til = linje.find(">")
                mail = linje[fra+1:til]

                liste.append(mail)
    return liste
while True:
    try:
        fil = input("Fil> ")
        set = mail_fra_fil(fil)
        break
    except:
        continue



#liste = mail_fra_fil("hadoop_1m_uft.txt")
with open("mail.txt", "w+") as file: #åpne ny fil
    for element in set:
        file.write(element + "\n")

