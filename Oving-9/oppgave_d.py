import random

class Question():
    def __init__(self, question, answer, alternatives):
        self.question = question
        self.answer = answer
        self.alternatives = alternatives


    def sjekk_svar(self, sjekk: int): #int : bestemmer at dette skal være et heltall
        return sjekk == self.answer

class Spiller():
    def __init__(self, name):
        self.name = name
        self.answer = ""
        self.poeng = 0

class gamer():
    def __init__(self, name, answer=0):
        self.name = name
        self.answer = answer

def les_spørsmål_fil(sporsmaalsfil):

 quiz=list()

 with open(sporsmaalsfil, "r", encoding="UTF8") as file:
        for line in file:
            line = line.strip("")
            line = line.split(":")
            quiz.append(Question(line[0], int(line[1]), line[2]))
        return quiz



if __name__=="__main__":
    spillere = [Spiller("Spiller1"), Spiller("Spiller2")]
    quiz = les_spørsmål_fil("sporsmaalsfil (1).txt")
    poeng = 0
    for question in quiz:
        print(question.question)
        for index, alternative in enumerate(question.alternatives.split(",")):
            print(f"{index}: {alternative} ")
        for spiller in spillere:
            spiller.answer = int(input(f"{spiller.name} > "))
        for spiller in spillere:
            if question.sjekk_svar(spiller.answer):
                print(f"Korrekt! Du er flink, {spiller.name}!")
                spiller.poeng += 1
            else:
                print(f"you trash bro, {spiller.name}!")
    for spiller in spillere:
        print(f"{spiller.name} fikk {spiller.poeng} poeng!")









        #int(input("hvor mange spillere?"))








