with open("sporsmaalsfil (1).txt", "r", encoding="UTF8") as file:
    while (line := file.readline().rstrip()):
        print(line)


