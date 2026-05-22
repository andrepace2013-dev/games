from turtle import *
import time
import random
Score=0
w=Screen()
w.setup(width=1100,height=1100)
dart=Turtle()
dart.shape('triangle')
dart.color('red')
dart.up()
dart.goto(0,-200)
dart.setheading(90)
baloons=[]
s=Turtle()
def score():
    s.clear()
    time.sleep(1.5)
    s.write('Score:{}'.format(Score),font=("Arial",16,"normal"),align='left')
def game_over():
    over=Turtle()
    over.hideturtle()
    over.color('red')
    over.write('GAME OVER',align='center')
    w.update()
    time.sleep(2)
    w.bye()
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
difficulty=0.001
intervile=7
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
        if dart.distance(i)<20:
            if i.bomb:
                game_over()
            else:
                Score+=10
                score()
            baloons.remove(i)
            i.hideturtle()
    game_speed=max(0.005,game_speed-difficulty)
    intervile=max(0.5,intervile-0.0005)
done()
