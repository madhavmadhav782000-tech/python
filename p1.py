from turtle import *
speed('fast')
pencolor('blue')
pensize(2)

side = 6
for i in range (side):
    fd(100)
    lt(360/side)
fd(50)
lt(360/side)

hideturtle()
mainloop()