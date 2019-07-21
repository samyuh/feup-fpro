import turtle
janela = turtle.Screen()

ninja = turtle.Turtle()
ninja.color(cor)
ninja.fillcolor(corfill)

ninja.begin_fill()
for i in range(lados):
    ninja.forward(comprimento)
    ninja.left(360/lados)
ninja.end_fill()

janela.exitonclick()
turtle.bye()