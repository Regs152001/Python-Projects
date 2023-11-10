import turtle 
window = turtle.Screen()

turtle.Screen()
turtle.title("Shapes")
turtle.Screen().bgcolor("black")
turtle.shape('turtle')
turtle.pensize(2)

#Oval
def drawoval(rad):
  for x in range(2):
     
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)

turtle.seth(-45)

turtle.penup()
turtle.goto(-250, -100)

turtle.pendown()

turtle.color('white', '#fcffff')
turtle.begin_fill()
drawoval(350)
turtle.end_fill()



#Eye Right

turtle.penup()
turtle.goto(-150, -100)
turtle.backward(100)

turtle.color('black', 'black')
turtle.begin_fill()

turtle.pendown()
turtle.circle(70)

turtle.end_fill()


#Middle draw to connect to Eye

turtle.penup()
turtle.goto(-60, -40)
turtle.backward(70)

turtle.pendown()
turtle.goto(120, 10)


#Eye Left

turtle.penup()
turtle.goto(120, -30)
turtle.pendown()

turtle.color('black', 'black')
turtle.begin_fill()

turtle.circle(70)

turtle.end_fill()

turtle.penup()
turtle.forward(200)

window.exitonclick()
