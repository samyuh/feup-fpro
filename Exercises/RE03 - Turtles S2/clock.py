import turtle

janela = turtle.Screen()
janela.bgcolor("lightgreen")

athena = turtle.Turtle()
athena.color("blue")
athena.shape("turtle")
athena.pensize(3)

athena.stamp()
athena.hideturtle()

for i in range(12):
    athena.penup()
    athena.forward(75)
    athena.pendown()
    athena.forward(15)
    athena.penup()
    athena.forward(25)
    athena.stamp()
    athena.backward(115)
    athena.right(360/12)
    
janela.exitonclick()
turtle.bye()