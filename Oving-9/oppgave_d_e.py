class Question:
    def __init__(self, question):
        self.question = question
        self.answer = []
        self.correct = 0

    def set_answer(self, value: int):
        self.correct = value

    def check_answer(self, val: int) ->bool:
        return val == self.correct_answer

    def add_alternative(self, alt: str):
        self.answer.append(alt)

    def __str__(self) -> str:
        result = ""
        result += "Q:"+self.question + "\n"
        for (j, a) in enumerate(self.answer):
            result += "[" + str(j) + "]: "+a+"\n"

        return result




def Sporsmaal():

    questions = []
    ans = []
    correct_ans = []

    List_1 = []
    with open("sporsmaalsfil.txt","r",encoding="UTF8") as txt_file:

        for linje in txt_file:
            linje_1=linje.split(":")




            linje_2=linje_1[2].strip(" []\n")

            linje_2= [x.strip() for x in linje_2.split(",")]

            if len(linje_2) < 4:

                linje_2.append("__")
                linje_2.append("__")


            questions.append(linje_1[0])

            correct_ans.append(linje_1[1])

            letters = ["a", "b", "c", "d"]
            cv = []
            for i in range(4):
                cv.append(letters[i] + ") "+linje_2[i])
            ans.append(cv)

        return questions, ans, correct_ans




if __name__== "__main_":



    print("****WELCOME TO THE GAME*****")

    antall_s=int(input("Antall spiller: "))
    score=dict()
    for i in range(antall_s):
        navn=input(f"Hva er navnet til spillerne {i+1}: ")
        score[navn]=0
    Test= Question(score)

    questions, ans, correct_answer = Sporsmaal()
    #score = 0
    counter = 1
    num = 0

    l_ans = []
    for i in correct_answer:
        if i.strip() == "0":
            l_ans.append("a")
        elif i.strip() == "1":
            l_ans.append("b")
        elif i.strip() == "2":
            l_ans.append("c")
        elif i.strip() == "3":
            l_ans.append("d")
        else:
            pass

    for q, a, c in zip(questions, ans, correct_answer):
        print(str(counter) + "." + q.strip())

        for x, y in zip(a, c):
            print(x)

        svar = dict()

        for spiller in score.keys():
            svar[spiller] = input("Skriv inn ans ({}): ".format(spiller)).lower()
            print("\n")

        for spiller in score.keys():
            if svar[spiller] == l_ans[num]:
                print("({}) Correct".format(spiller))
                score[spiller] += 1
                # print("*"*40)
            else:
                print("({}) Feil, svaret er: ".format(spiller), l_ans[num])

        print("*"*40)

        num += 1
        counter += 1
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")



