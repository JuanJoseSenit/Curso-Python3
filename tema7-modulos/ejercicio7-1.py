import turtle

window = turtle.Screen()
cursor = turtle.Turtle()
cursor.left(90)
cursor.forward(90)
cursor.right(90)

for x in range(1,25):
    cursor.left(5)
    cursor.forward(45)
    cursor.left(100)
    cursor.forward(45)
window.exitonclick()