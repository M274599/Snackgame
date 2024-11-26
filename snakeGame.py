import turtle
import time
import random

delay=0.1
score=0
max_score=0

# game window
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#243642")
wn.setup(width=600,height=600)
wn.cv._rootwindow.resizable(False,False)


#snake head
head=turtle.Turtle()
head.shape("square")
head.color("green")
head.goto(0,0)
head.speed(0)




#screen updated
def update_screen():
    wn.update()
    time.sleep(delay)


while True:
    update_screen()








