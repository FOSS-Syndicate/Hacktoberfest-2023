from turtle import *
import tkinter
import random 

setup(800, 800)

#s = size of section 
#l = level of recursion
def tiling(x,y,s,l):

    # final level of recursion 
    #Draw
    if l == 0:

        if random.random() > 0.5:

            #Vertical
            penup()
            goto(x,y-s)
            pendown()

            fillcolor('white')
            begin_fill()
            #Begin Circle
            circle(3)
            #Line
            goto(x,y+s)
            #End Circle 
            circle(3)
            end_fill()

        else:
            #Horizontal
            penup()
            goto(x-s,y)
            pendown()

            fillcolor('white')
            begin_fill()
            #Begin Circle
            circle(3)
            #Line
            goto(x+s,y)
            #End Circle
            circle(3)
            end_fill()
    
    # Split the recursion and go to next level 
    else:
        s /= 2
        l -= 1
        tiling(x-s,y+s,s,l)
        tiling(x+s,y+s,s,l)
        tiling(x-s,y-s,s,l)
        tiling(x+s,y-s,s,l)

# line_color = random('blue', 'red', 'black', 'cyan', 'magneta')

bgcolor('black')
color('white')
hideturtle()
width(2)
speed(0)
tiling(0,0,250,4)

exitonclick()