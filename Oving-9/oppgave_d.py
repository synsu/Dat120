class Question():
    def __init__(self, question, answer, alternatives):
        self.question = question
        self.answer = answer
        self.alternatives = alternatives

    def korrekt_svar_tekst(self):
        svar = self.alternatives[self.answer]
        return svar

class gamer():
    def __init__(self, name, answer=0):
        self.name= name
        self.answer = answer

def les_spørsmål_fil(sporsmaalsfil):

 Ques_list=[]

 with open(sporsmaalsfil, "r", encoding="UTF8") as file:
        for line in file:
            line = line.strip("")
            line = line.split(":")
            Ques_list.append(Question(line[0], int(line[1]), line[2]))
        return Ques_list


if __name__=="__main__":

    les_spørsmål_fil("sporsmaalsfil (1).txt")



        #int(input("hvor mange spillere?"))








