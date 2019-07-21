import turtle

janela = turtle.Screen()
wendy = turtle.Turtle()
wendy.goto(-50,0)

for i in range(4):
    wendy.forward(100)
    wendy.left(360/4)

for i in range(3):
    wendy.forward(100)
    wendy.left(360/3)

for i in range(6):
    wendy.forward(100)
    wendy.left(360/6)

for i in range(8):
    wendy.forward(100)
    wendy.left(360/8)

janela.exitonclick()
turtle.bye()