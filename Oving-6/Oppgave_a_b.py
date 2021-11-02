import matplotlib.pyplot as plt
file = open("trykk_og_temperaturlogg.csv", "r")
line = file.readline()
print(line)


date_and_time = []
time_since_start = []
abso_pressure = []
temp = []


for line in file:
    line = line.replace(",", ".")
    r_list = line.split(";")
    date_and_time.append(r_list[0])
    time_since_start.append(float(r_list[1]))
    abso_pressure.append(float(r_list[3]))
    temp.append(float(r_list[4]))
print(len(temp), len(time_since_start)) #nummer av antallet

try:
    plt.subplot(2,2,1)
    plt.plot(time_since_start, temp, label="Temp")
    plt.xlabel("tid i sekund")
    plt.ylabel("temp i celcius")
    plt.subplot(2,2,2)
    plt.plot(time_since_start, abso_pressure, "-", label = "Pressure")
    plt.xlabel("tid i sekund")
    plt.ylabel("trykk i bar")
    #plt.legend()
    plt.show()
    file.close()
except ValueError:
    print("Unexpected value")

















