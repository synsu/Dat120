
file = open("trykk_og_temperaturlogg.csv")
line = file.readline()

siste_tid = 0


for line in file:
    line = line.replace(",", ".")
    r_list = line.split(";")
    ny_tid = int(r_list[1])
    if ny_tid - siste_tid > 10:
        print(f"Mangler målinger {r_list[0]}:{(int(r_list[1])-10)%60}") #modulo 60, reminder
    siste_tid = ny_tid


 
