from turtle import *
import time
import random
w=Screen()
w.setup(width=1100,height=1100)
dart=Turtle()
dart.shape('triangle')
dart.color('red')
dart.up()
dart.goto(0,-200)
dart.setheading(90)
baloons=[]
def makebaloon():
    baloon=Turtle()
    baloon.up()
    baloon.shape('circle')
    colour=random.choice(['red','blue','green','yellow'])
    baloon.color(colour)
    x=random.randint(-240,240)
    baloon.goto(x,500)
    speed1=random.uniform(1,10)
    baloon.speed=speed1
    if random.random()<0.2:
        baloon.color('black')
        baloon.bomb=True
    else:
        baloon.bomb=False
    baloons.append(baloon)
def left():
    x=dart.xcor()
    if x>-200:
        dart.setx(x-10)
def right():
    x=dart.xcor()
    if x<200:
        dart.setx(x+10)
w.listen()
w.onkey(left,'Left')
w.onkey(right,'Right')
game_speed=0.02
difficylty=0.001
intervile=2
last_spawn_time=time.time()
while True:
    w.update()
    current_time=time.time()
    if current_time-last_spawn_time>intervile:
        makebaloon()
        last_spawn_time=current_time
    for i in baloons[:]:
        i.sety(i.ycor()-i.speed)
        if i.ycor()<-250:
            baloons.remove(i)
            i.hideturtle()

done()