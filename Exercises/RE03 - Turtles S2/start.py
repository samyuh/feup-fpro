import turtle

n = int(input("Number of sides: "))

janela = turtle.Screen()
janela.bgcolor("blue")

zeus = turtle.Turtle()
zeus.color("white")
zeus.shape("circle")

zeus.pensize(3)
zeus.stamp()
zeus.hideturtle()

for i in range(n):
    zeus.forward(165)
    zeus.stamp()
    zeus.backward(165)
    zeus.right(360/n)
    
janela.exitonclick()
turtle.bye()