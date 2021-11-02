import matplotlib.pyplot as plt
file = open("trykk_og_temperaturlogg.csv", "r")
line = file.readline()

print(line)
temp = []


for line in file:
    line = line.replace(",", ".")
    r_list = line.split(";")
    temp.append(float(r_list[4]))
print(temp)

x = temp
plt.hist(x, bins=10)
plt.xlabel("temp")
plt.show()
