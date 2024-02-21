from turtle import *


#we want to paint a house

#step 1: draw a square
shape("turtle")
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#and of spuare

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)  #heit of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(50,50)
pendown()

color("brown")
right(60)
forward(40)

right(90)
forward(60)

right(90)
forward(40)

right(90)
forward(60)

penup()
goto(150,50)
pendown()

left(90)
forward(40)

left(90)
forward(60)

left(90)
forward(40)

left(90)
forward(60)




exitonclick()