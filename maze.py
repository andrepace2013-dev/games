from turtle import*
t=Turtle()
t.speed(0)
t.shape('square')
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
      'XXX XX   XXXXX',
      'XXX XXXXXXXXXX',
      'XXX          X',
      'XXXXXX       X',
      'XXXXXXXXXXXX F']
p=Turtle()
p.shape('turtle')
o=[]
def create_maze():
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
done()