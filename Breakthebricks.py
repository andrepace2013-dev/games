from turtle import*
import time
Score=0
game_started=False
w=Screen()
w.setup(width=600, height=400)
w.bgcolor("black")
p=Turtle()
p.shape("square")
p.color("white")
p.penup()
p.speed(0)
p.goto(0, -180)
p_width=120
b=Turtle()
S=Turtle()
b.shape("circle")
b.color("red")
b.penup()
b.goto(0,0)
b.dy=-2
b.dx=-2
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for row in range(4):
    for col in range(-250, 300, 80): 
        brick = Turtle() 
        brick.shape("square") 
        brick.color(colors[row])
# Different colors for each row
        brick.penup()
        brick.speed(0)
        brick.goto(col, 150 - (row*30))
        bricks.append(brick)
def score():
    S.clear()
    S.color('white')
    S.write('Score:{}'.format(Score),font=("Arial",16,"normal"),align='left')
def start_game(x,y): 
    global game_started 
    game_started = True
def left():
    x=p.xcor()
    if x>-280:
        p.setx(x-10)
def right():
    x=p.xcor()
    if x<280:
        p.setx(x+10)
w.listen()
w.onkey(left,'Left')
w.onkey(right,'Right')
w.onclick(start_game)
while True: 
    w.update() 
    time.sleep(0.01)
    if not game_started:
        continue 
        # Skip the loop if the game hasn't started yet
        # Move the ball
    b.setx(b.xcor() + b.dx) 
    b.sety(b.ycor() + b.dy)
    if b.xcor()>290 or b.xcor()<-290:
        b.dx*=-1
    if b.ycor()>190:
        b.dy*=-1
    if b.ycor()<-190:
        b.goto(0,0)
        b.dy*=-1
        game_started=False
        Score=0
        score()
    if(b.ycor()>-180 and b.ycor()<-170) and (p.xcor() - p_width // 2 < b.xcor() < p.xcor() + p_width // 2):
        b.dy *= -1
    for i in bricks:
        if abs(b.xcor()-i.xcor())<40 and abs(b.ycor()-i.ycor())<15:
            b.dy*=-1
            i.hideturtle()
            bricks.remove(i)
            Score+=10
            score()
done()
