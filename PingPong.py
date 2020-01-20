import turtle

wn = turtle.Screen()
wn.title("PingPong KarolinyQ")
wn.bgcolor("misty rose")
wn.setup(width=800, height=600)
wn.tracer(0)

# Wynik
wynik_a = 0
wynik_b = 0

# Paletka A
paletka_a = turtle.Turtle()
paletka_a.speed(0)
paletka_a.shape("square")
paletka_a.color("hot pink")
paletka_a.shapesize(stretch_wid=5,stretch_len=1)
paletka_a.penup()
paletka_a.goto(-350, 0)



# Paletka B
paletka_b = turtle.Turtle()
paletka_b.speed(0)
paletka_b.shape("square")
paletka_b.color("hot pink")
paletka_b.shapesize(stretch_wid=5,stretch_len=1)
paletka_b.penup()
paletka_b.goto(350, 0)


# Pilka
pilka = turtle.Turtle()
pilka.speed(0)
pilka.shape("square")
pilka.color("dim gray")
pilka.penup()
pilka.goto(0, 0)
pilka.dx = 0.25
pilka.dy = 0.25

# Dlugopis
pen= turtle.Turtle()
pen.speed(0)
pen.color("dim gray")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Gracz A: 0 Gracz B: 0", align="center",font=("Courier", 24, "bold"))

# Funkcje
def paletka_a_gora():
    y = paletka_a.ycor()
    y += 20
    paletka_a.sety(y)

def paletka_a_dol():
    y = paletka_a.ycor()
    y -= 20
    paletka_a.sety(y)

def paletka_b_gora():
    y = paletka_b.ycor()
    y += 20
    paletka_b.sety(y)

def paletka_b_dol():
    y = paletka_b.ycor()
    y -= 20
    paletka_b.sety(y)


# Przyciski na klawiaturze
wn.listen()
wn.onkeypress(paletka_a_gora, "w")
wn.onkeypress(paletka_a_dol, "s")
wn.onkeypress(paletka_b_gora, "Up")
wn.onkeypress(paletka_b_dol, "Down")


# Petla glownej gry
while True:
    wn.update()

    # Ruch pilki
    pilka.setx(pilka.xcor() + pilka.dx)
    pilka.sety(pilka.ycor() + pilka.dy)

    # Sprawdzanie granicy
    if pilka.ycor() > 290:
        pilka.sety(290)
        pilka.dy *= -1

    if pilka.ycor() < -290:
        pilka.sety(-290)
        pilka.dy *= -1

    if pilka.xcor() > 390:
        pilka.goto(0,0)
        pilka.dx *= -1
        wynik_a += 1
        pen.clear()
        pen.write("Gracz A: {} Gracz B: {}".format(wynik_a, wynik_b), align="center", font=("Courier", 24, "bold"))

    if pilka.xcor() < -390:
        pilka.goto(0,0)
        pilka.dx *= -1
        wynik_b += 1
        pen.clear()
        pen.write("Gracz A: {} Gracz B: {}".format(wynik_a, wynik_b), align="center", font=("Courier", 24, "bold"))

    # Spotkanie pilki i paletki
    if (pilka.xcor() > 340 and pilka.xcor() < 350) and (pilka.ycor() < paletka_b.ycor() + 40 and pilka.ycor() > paletka_b.ycor() -40):
        pilka.setx(340)
        pilka.dx *= -1

    if (pilka.xcor() < -340 and pilka.xcor() < -350) and (pilka.ycor() < paletka_a.ycor() + 40 and pilka.ycor() > paletka_a.ycor() -40):
        pilka.setx(-340)
        pilka.dx *= -1