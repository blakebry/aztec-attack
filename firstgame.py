import turtle
import os
import math
import random



#set up screen
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("First Game")
screen.bgpic("background.gif")

#register the shapes
turtle.register_shape("npc.gif")
turtle.register_shape("player.gif")
turtle.register_shape("bullet.gif")

#border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set score to zero
score = 0


#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,305)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


#create player
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#player movement
playerspeed = 15

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -285:
        x = - 285
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 285:
        x = 285
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move bullet to just above player
        x = player.xcor()
        y = player.ycor() + 10 
        bullet.setposition(x, y)
        bullet.showturtle()
    if not bullet.isvisible():
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition (x,y)
        bullet.showturtle()
# collision
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 47:
        return True
    else:
        return False

#number of npcs
number_of_npcs = 5

#create empty list of npcs
npcs = []

#add npcs to list
for i in range(number_of_npcs):
    #create the enemy
    npcs.append(turtle.Turtle())
for npc in npcs: 
    npc.color("purple")
    npc.shape("npc.gif")
    npc.penup()
    npc.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    npc.setposition(x,y)

npcspeed = 3

#player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.4, 0.4)
bullet.hideturtle()

bulletspeed = 7

#define bullet state

bulletstate = "ready"

#keybinds
turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire_bullet, "space")

#game loop
while True:

    for npc in npcs:
        #npc movement
        x = npc.xcor()
        x += npcspeed
        npc.setx(x)

        #move the npc back and down
        if npc.xcor() > 280:
            #move all npcs down
            for n in npcs:
                y = n.ycor()
                y -= 40
                n.sety(y)
            #change npcs direction
            npcspeed *= -1
            

        if npc.xcor() < -280:
            #move all npcs down
            for n in npcs:
                y = n.ycor()
                y -= 40
                n.sety(y)
            #change npcs direction
            npcspeed *= -1
    

        if bullet.isvisible():
            y = bullet.ycor() + bulletspeed
            bullet.sety(y)

 #collision between bullet/npc
        if isCollision(bullet, npc):
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset npc
            x = random.randint(-200,200)
            y = random.randint(100,250)
            npc.setposition(x,y)
            npcspeed += 2.75
            
            #update score
            score += 1
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        
            
        #enemy/player collision
        if isCollision(player, npc):
            player.hideturtle()
            npc.hideturtle()
            print ("you lost")
            break

        #bullet movement
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        #bullet border hit
        if bullet.ycor() > 275:
            score_pen = turtle.Turtle()
            score_pen = turtle.Turtle()
            score_pen.speed(0)
            score_pen.color("Red")
            score_pen.penup()
            score_pen.setposition(-295,-100)
            scorestring = "GAME OVER" 
            score_pen.write(scorestring, False, align="left", font=("Arial", 73, "bold"))
            score_pen.hideturtle()
            break 
            

       
        
        
    
    


