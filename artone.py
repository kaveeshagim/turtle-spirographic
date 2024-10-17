import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'dark red']

for number in range(400):
    t.forward(number+1) # forward() draws a straight line
    t.right(89) # right() gives the angle
    t.pencolor(colors[number%2]) # to switch between red and dark red
turtle.done()