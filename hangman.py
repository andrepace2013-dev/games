import random
from turtle import *
screen=Screen()
screen.setup(width=400,height=400)
screen.bgcolor('white')
pen=Turtle()
pen.color('black')
pen.up()
pen.goto(0,-50)
pen.down()
pen.left(90)
pen.forward(200)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.speed(0)
def head():
    pen.setheading(0)
    for i in range(36):
        pen.forward(3)
        pen.right(10)
    pen.up()
    pen.goto(102,65)
    pen.setheading(270)
    pen.down()
def body():
    pen.forward(70)
    pen.left(45)
def leftleg():
    pen.forward(20)
    pen.up()
    pen.goto(102,-5)
    pen.right(90)
    pen.down()
def rightleg():
    pen.forward(20)
    pen.up()
    pen.goto(102,50)
    pen.down()
def rightarm():
    pen.forward(20)
    pen.up()
    pen.goto(102,50)
    pen.left(90)
    pen.down()
def leftarm():
    pen.forward(20)
    pen.up()
    pen.goto(91,75)
    pen.down()
def smile():
    for i in range(13):
        pen.forward(2)
        pen.left(8)
    pen.up()
    pen.goto(94,88)
    pen.right(145)
    pen.down()
def eyes():
    pen.forward(7)
    pen.up()
    pen.goto(110,88)
    pen.down()
    pen.forward(7)
head_drawn = False
body_drawn = False
leftleg_drawn = False
rightleg_drawn = False
rightarm_drawn = False
leftarm_drawn = False
smile_drawn = False
eyes_drawn = False
print('WELCOOME TO HANGMAN GAME!!!')
try:
    print('1=Easy \n 2=medium \n 3=hard \n 4=IMPOSSIBLE \n 5=choose your own word')
    diff=int(input("Select you difficulty"          ))
    if diff==1:
        easy=("hat","bone",'cat','dog','sun','Pen','Hat','Box','Car','Bed','Map','key',"book", "tree", "ball", "fish", "door", "hand", "bird", "moon", "star", "rock")
        word=random.choice(easy)
    elif diff==2:
        medium=("forest", "window", "planet", "bridge", "garden", "market", "button", "pencil", "bottle", "castle","island", "letter", "mother", "friend", "circle", "school", "office", "animal", "street", "family")
        word=random.choice(medium)
    elif diff==3:
        hard=("mountain", "building", "elephant", "hospital", "notebook", "sandwich", "computer", "passport","triangle", "umbrella", "calendar", "airplane", "dinosaur", "backpack", "painting", "headline")
        word=random.choice(hard)
    elif diff==4:
        imp=("archaeology","counterattack","microbiology","university","international","photosynthesis","electrocardiogram","psychotherapy","radioimmunoassay","antidisestablishment","floccinaucinihilipilification","pseudopseudohypoparathyroidism","thyroparathyroidectomized")
        word=random.choice(imp)
    elif diff==5:
        word=input('What word would you like to choose?          ')
    else:
        print("Ivalid Input")
    hidden=["_"]*len(word)
    print(" ".join(hidden))
    ch=8
    cur=0
    while "_" in hidden and cur<ch:
            guess=input('Enter a letter for guess.          ')
            if guess in word.lower():
                for i in range(len(word)):
                    if word[i].lower()==guess:
                        hidden[i]=guess
            else:
                cur+=1
            print(" ".join(hidden))
            if cur==1 and not head_drawn:
                head()
                head_drawn = True
            if cur==2 and not body_drawn:
                body()
                body_drawn = True
            if cur==3 and not leftleg_drawn:
                leftleg()
                leftleg_drawn = True
            if cur==4 and not rightleg_drawn:
                rightleg()
                rightleg_drawn = True
            if cur==5 and not rightarm_drawn:
                rightarm()
                rightarm_drawn = True
            if cur==6 and not leftarm_drawn:
                leftarm()
                leftarm_drawn = True
            if cur==7 and not smile_drawn:
                smile()
                smile_drawn = True
            if cur==8 and not eyes_drawn:
                eyes()
                eyes_drawn = True
                pen.up()
                pen.goto(0,0)
                done()      
    if '_'not in hidden:
        print('CONGRADULATIONS HE ONLY GOT SOME OF HIS LIMBS ON THE ROPE!!!')
    else:
        print('You lost!!! The man got fully hanged.')
        print(word)
except ValueError:
    print('Invalid input. Only enter numbers from 1-5.')
