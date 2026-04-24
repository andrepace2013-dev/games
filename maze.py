from turtle import*
import time
t=Turtle()
t.speed(0)
t.shape('square')
w=Screen()
w.bgcolor("#78BE2E")
maze=['XXXXXXXXXXXXXX',
      'X            X',
      'XX XX XXXX XXX',
      'XX XX XXXX XXX',
      'X   XXX      X',
      'XXXXXXX XXXX X',
      'X       XXXX X',
      'X XXXXXXXXXX X',
      'X XXXXXXXX   X',
      'X    XXX     X',
      'XXX XXXX XXXXX',
      'XXX X    XXXXX',
      'XXX XXXX     X',
      'XXX    XXXXXXX',
      'XXXXXX       X',
      'XXXXXXXXXXXX F']
p=Turtle()
p.shape('turtle')
o=[]
def create_maze():
    global finish
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            charachter=maze[y] [x]
            screen_x =-288+(x*24)
            screen_y=288-(y*24)
            if charachter=='X':
                obstacle=Turtle()
                obstacle.speed(0)
                obstacle.shape('square')
                obstacle.color('black')
                obstacle.penup()
                obstacle.goto(screen_x, screen_y)
                o.append(obstacle)
            elif charachter=='F':
                finish=Turtle()
                finish.shape('circle')
                finish.color('red')
                finish.up()
                finish.goto(screen_x,screen_y)
def valide_move(x,y):
    for i in o:
        if i.xcor()==x and i.ycor()==y:
            return False
    return True
def win():
    if p.distance(finish)<10:
        p.hideturtle()
        w.bye()
        print('Congradulations you completed the maze.')
def move_up():
    p.setheading(90)
    x=p.xcor()
    y=p.ycor()+24
    if valide_move(x,y):    
        p.goto(x,y)
        win()
def move_right():
    p.setheading(0)
    x=p.xcor()+24
    y=p.ycor()
    if valide_move(x,y):
        p.goto(x,y)
        win()
def move_down():
    p.setheading(270)
    x=p.xcor()
    y=p.ycor()-24
    if valide_move(x,y):
        p.goto(x,y)
        win()
def move_left():
    p.setheading(90)
    x=p.xcor()-24
    y=p.ycor()
    if valide_move(x,y):
        p.goto(x,y)
        win()
w.listen()
w.onkey(move_up,'Up')
w.onkey(move_right,'Right')
w.onkey(move_down,'Down')
w.onkey(move_left,'Left')
p.up()
before=time.time()
create_maze()
p.goto(-264,264)
done()
