
#we want to paint a house

from turtle import*
shape("turtle")
speed(15)
#house

color("black")
width(7)
#square
forward(200)   
left(90)
forward(200)   
left(90)
forward(200)   
left(90)
forward(200)   
left(90)
#door

forward(70)

color("yellow")
begin_fill()
left(90)
forward(100)  #door height
right(90)
forward(50)    #door lenght
right(90)
forward(100)
end_fill()
#roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window
color("blue")
penup()
goto(20,170)
pendown()
right(240)
forward(50)
right(90)  
forward(50)
right(90)  
forward(50)
right(90)  
forward(50)
right(90)
forward(25)
right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)




exitonclick()