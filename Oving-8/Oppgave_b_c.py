#flervalgsspørsmål:
#skal ha en spørsmålstekst, ei liste med svaralternativer
#(hvert svaralternativ er en tekststreng), og et tall som sier hvilket av svaralternativene som er
#korrekt


class A():
    def __init__(self, question, answer, alternatives): #returnerer ingenting
        self.question = question
        self.answer = answer
        self.alternatives = alternatives

    def __str__(self): #denne klassen returnerer en streng
        tekst = self.question + "\n"
        for altNummer, altTekst in enumerate(self.alternatives):
            tekst += f"    {altNummer + 1}: {altTekst} \n"
        return tekst

    def sjekk_svar(self, sjekk: int): #int : bestemmer at dette skal være et heltall
        return sjekk == self.answer

quiz = list() #eller quiz = []

quiz.append(A("Hvor mange studenter er i denne klassen?", 4, [1, 10, 5, 95, 200]))
quiz.append(A("Hva er hovedstaden i Norge?", 2, ["Berlin", "Oslo", "København", "Paris"]))

for spm in quiz:
    print(spm)

    valg = int(input(f"Ditt svar er (1-{len(spm.alternatives)}): "))
    if spm.sjekk_svar(valg):
        print("Veldig bra!")
    else:
        print("Prøv igjen..")




