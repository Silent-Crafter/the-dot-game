#!/usr/bin/python3
import turtle
from functions import *

highscore = 0
score = 0
speed = 1.8

#background
bg = turtle.Screen()
bg.title("The Dot Game")
bg.setup(width=800,height=600)
bg.tracer(0)

#dot
dot = turtle.Turtle()
dot.color("black")
dot.pu()
dot.shape("square")
dot.direction = 'stop'

#pen
pen = turtle.Turtle()
pen.color("red")
pen.hideturtle()
pen.speed(0)
pen.up()
pen.goto(-350,250)
pen.write("Highscore = 0",move=True,align="left",font=('Arial',26,'normal'))
pen.goto(150,250)
pen.write("Score = 0",move=True,align="left",font=('Arial',26,'normal'))

#boundary
boundary = turtle.Turtle()
boundary.color('black')
boundary.hideturtle()
boundary.pu()
boundary.goto(-370,249)
boundary.pd()
boundary.goto(370,249)
boundary.goto(370,-249)
boundary.goto(-370,-249)
boundary.goto(-370,249)
boundary.pu()

#food
food = turtle.Turtle()
food.hideturtle()
food.shape('circle')
food.color('green')
food.direction = 'stop'
food.pu()

#bfood
bfood = turtle.Turtle()
bfood.hideturtle()
bfood.pu()
bfood.shape('circle')
bfood.color('red')
bfood.shapesize(3,3,0)
bfood.goto(1000,1000)
bfood.direction = 'stop'

#game tuple to store ALL vars
gamevars = (bg,boundary,food,bfood,dot,pen)

#key-bindings
bg.listen()
bg.onkeypress(lambda: go_up(gamevars),'w')
bg.onkeypress(lambda: go_right(gamevars),'d')
bg.onkeypress(lambda: go_left(gamevars),'a')
bg.onkeypress(lambda: go_down(gamevars),'s')
bg.onkeypress(lambda: go_up(gamevars),'Up')
bg.onkeypress(lambda: go_right(gamevars),'Right')
bg.onkeypress(lambda: go_left(gamevars),'Left')
bg.onkeypress(lambda: go_down(gamevars),'Down')
bg.onkeypress(lambda: close(gamevars),'Escape')

spawn(food,bfood)

#gameloop
while True:
    try:

        bg.update()
        
        move(gamevars,speed)

        """
        # Teleportation thingy
        if dot.xcor() <= -365:
            dot.setx(abs(dot.xcor())-15)

        elif dot.ycor() <= -245
            dot.sety(abs(dot.ycor())-15)

        elif :
            dot.setx(15-dot.xcor())

        elif :
            dot.sety(15-dot.ycor())
        """

        #Game-over
        if dot.xcor() <=-360 or dot.ycor() <= -245 or dot.xcor() >= 365 or dot.ycor() >= 245:
            dot.direction = 'stop'
            
            disable_keys(gamevars)
            
            food.goto(1000,1000)
            bfood.goto(1000,1000)
            food.hideturtle()
            bfood.hideturtle()
            dot.goto(0,0)
            bg.update()
            score = 0
            speed = 1.8
            display_score(pen,score,highscore)
            bg.update()
            
            spawn(food,bfood)
            countdown(gamevars)
            dot.home()
            
            enable_keys(gamevars)

            bg.update()

        #food collision
        if dot.distance(bfood) <= 35:
            bfood.hideturtle()
            bfood.goto(1000,1000) #Send food to heaven

            score += 10
            if score >= highscore:
                highscore = score

            speed += 1
            display_score(pen,score,highscore)
            spawn(food,bfood)

        if dot.distance(food) <= 20:
            food.hideturtle()
            food.goto(1000,1000) #Send food to heaven

            score += 1
            if score >= highscore:
                highscore = score

            speed += 0.1
            display_score(pen,score,highscore)
            spawn(food,bfood)

        #speed of program
        time.sleep(0.01)

    #Close the program
    except turtle.Terminator:
        exit()

turtle.done()
