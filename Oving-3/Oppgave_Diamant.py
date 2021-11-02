import turtle
import math #for å kunne regne regnestykker

def draw_diamond(length): #tegne en firkant(funksjon)
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def move_turtle(lengde): #funskjon for å flytte turtle til neste diamant
    turtle.left(135)
    turtle.penup()
    turtle.forward(lengde)
    turtle.pendown()
    turtle.right(135)

def get_new_length(length, ekstra):
    return length + ekstra/math.sin(math.radians(45))
#hypotenusen siden det må legges på for å få rett avstand mellom diamantene på alle sider, og for hver diamant

#Init #starter her
turtle.right(45) #vinkelen som turtle skal stå i når den begynner å tegne(ikke i funksjonen)
turtle.pensize(1)
turtle.speed(20)

lengde = 80
ekstra = 40

antall = int(input("Hvor mange diamanter > "))

for i in range(antall): #lager så mange diamanter som brukeren skriver inn
    draw_diamond(lengde)
    move_turtle(ekstra)
    lengde = get_new_length(lengde, ekstra)


turtle.done()
