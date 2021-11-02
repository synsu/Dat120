wordlist={}  # eller ordliste = Dict()

with open("oving_1_rein_tekst.txt", encoding="UTF-8") as file:
    linenr = 0
    for line in file:
        linenr = linenr+1
        for word in line.strip().split():  #linje er tekst, strip er funksjon for alle objekter av typen tekst.
            if word not in wordlist:
                wordlist[word] = linenr

for word, linenr in wordlist.items():
    print(f'Ordet "{word}" forekommer først på linje nummer {linenr}')



























