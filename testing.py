import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#setupscreen
wn = turtle.Screen()
wn.title("i'm cooler than color")
wn.setup(width=3840, height=2160) 
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed()
food.shape("square")
food.color("orange")
food.penup()

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")

pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions
def go_up():
       if head.direction != "down":
              head.direction = "up"

def go_down():
       if head.direction != "up":
              head.direction = "down" 

def go_left 
       if head.direction != "up":
              head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboardbindings
wn.listen
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#maingameloop
while True


 
