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
print('WELCOOME TO HANGMAN GAME!!!')
try:
    print('1=Easy \n 2=medium \n 3=hard \n 4=IMPOSSIBLE \n 5=choose your own word')
    diff=int(input("Select you difficulty"          ))
    if diff==1:
        easy=("hat","bone",'cat','dog','sun','Pen','Hat','Box','Car','Bed','Map','key'"book", "tree", "ball", "fish", "door", "hand", "bird", "moon", "star", "rock")
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
    ch=6
    cur=0
    while "_" in hidden:
        if cur<=ch:
            guess=input('Enter a letter for guess.          ')
            if guess in word.lower():
                for i in range(len(word)):
                    if word[i].lower()==guess:
                        hidden[i]=guess
            else:
                cur+=1
            print(" ".join(hidden))
        else:
            print('You lost!!! The man got fully hanged.')
            print(word)
            break
    if '_'not in hidden:
        print('CONGRADULATIONS HE ONLY GOT SOME OF HIS LIMBS ON THE ROPE!!!')
except ValueError:
    print('Invalid input. Only enter numbers from 1-5.')