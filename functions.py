import time
from random import randint
import turtle

#-----TUPLE POSITIONS-----
# => bg = 0
# => boundary = 1
# => food = 2
# => bfood = 3
# => dot = 4
# => pen = 5
#-------------------------

def disable_keys(gamevars):
    gamevars[0].listen()
    gamevars[0].onkeypress(None,'w')
    gamevars[0].onkeypress(None,'d')
    gamevars[0].onkeypress(None,'a')
    gamevars[0].onkeypress(None,'s')
    gamevars[0].onkeypress(None,'Up')
    gamevars[0].onkeypress(None,'Right')
    gamevars[0].onkeypress(None,'Left')
    gamevars[0].onkeypress(None,'Down')
    gamevars[0].onkeypress(None,'Escape')

def enable_keys(gamevars):
    gamevars[0].listen()
    gamevars[0].onkeypress(lambda: go_up(gamevars),'w')
    gamevars[0].onkeypress(lambda: go_right(gamevars),'d')
    gamevars[0].onkeypress(lambda: go_left(gamevars),'a')
    gamevars[0].onkeypress(lambda: go_down(gamevars),'s')
    gamevars[0].onkeypress(lambda: go_up(gamevars),'Up')
    gamevars[0].onkeypress(lambda: go_right(gamevars),'Right')
    gamevars[0].onkeypress(lambda: go_left(gamevars),'Left')
    gamevars[0].onkeypress(lambda: go_down(gamevars),'Down')
    gamevars[0].onkeypress(lambda: close(gamevars),'Escape')

def countdown(gamevars):
    
    gamevars[4].hideturtle()
    gamevars[2].hideturtle()
    gamevars[3].hideturtle()

    cd = turtle.Turtle()
    cd.pu()
    cd.color('blue')
    cd.goto(0,-80)
    cd.hideturtle()

    for i in range(3):
        cd.clear()
        cd.write("{}".format(3-i), align="center", font = ("Kristen ITC", 120, "bold"))
        gamevars[0].update()
        gamevars[4].direction = 'stop'
        gamevars[4].home()
        time.sleep(1)
    cd.clear()

    gamevars[3].showturtle()
    gamevars[2].showturtle()
    gamevars[4].showturtle()
    gamevars[4].direction = 'stop'
    del cd

def exitprogram(gamevars):
    gamevars[0].bye()

def close(gamevars):
    unload(gamevars)

    close = turtle.Turtle()
    close.speed(0)
    close.color("white")
    turtle.Screen().bgcolor('black')
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    close.write("Press ESC again to exit", align="center", font = ("Courier", 24, "normal"))
    gamevars[0].listen()
    gamevars[0].onkeypress(lambda: exitprogram(gamevars), "Escape")

def go_up(gamevars):
    if not gamevars[4].direction == 'down':
        gamevars[4].direction = 'up'

def go_right(gamevars):
    if not gamevars[4].direction == 'left':
        gamevars[4].direction = 'right'

def go_down(gamevars):
    if not gamevars[4].direction == 'up':
        gamevars[4].direction = 'down'

def go_left(gamevars):
    if not gamevars[4].direction == 'right':
        gamevars[4].direction = 'left'

def move(gamevars,speed):
    if gamevars[4].direction == 'up':
        y = gamevars[4].ycor()
        gamevars[4].sety(y+speed)

    if gamevars[4].direction == 'down':
        y = gamevars[4].ycor()
        gamevars[4].sety(y-speed)

    if gamevars[4].direction == 'left':
        x = gamevars[4].xcor()
        gamevars[4].setx(x-speed)

    if gamevars[4].direction == 'right':
        x = gamevars[4].xcor()
        gamevars[4].setx(x+speed)

#food-spawner
def spawn(food,bfood):

    if randint(1,100) % 13 == 0:
        if not bfood.isvisible():
            bfood.goto(randint(-355,355), randint(-235,235))
            bfood.showturtle()

    if not food.isvisible():
        food.goto(randint(-355,355), randint(-235,235))
        food.showturtle()

#score display
def display_score(pen,score,highscore):
    pen.clear()
    pen.color('red')
    pen.goto(-350,250)
    pen.write(f"Highscore = {highscore}",move=True,align="left",font=('Arial',26,'normal'))
    pen.goto(150,250)
    pen.write(f"Score = {score}",move=True,align="left",font=('Arial',26,'normal'))

def unload(gamevars):
    gamevars[4].direction = 'stop'
    gamevars[2].hideturtle()
    gamevars[3].hideturtle()
    gamevars[4].hideturtle()
    del gamevars