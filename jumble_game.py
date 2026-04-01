import random
print('WELCOOME TO JUMBLE WORD GAME!!!')
while True:
    try:
        print('1=Easy \n 2=medium \n 3=hard \n 4=IMPOSSIBLE \n 5=exit')
        diff=int(input("Select you difficulty"          ))
        if diff==1:
            easy=("hat","bone",'Cat','Dog','Sun','Pen','Hat','Box','Car','Bed','Map','key'"book", "tree", "ball", "fish", "door", "hand", "bird", "moon", "star", "rock")
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
            break
        else:
            print("Ivalid Input")
        wl=list(word)
        random.shuffle(wl)
        print(''.join(wl))
        hint=input('Do you want a hint?(Y/N)            ').upper()
        if hint=='Y':
            print('The first letter of the word is '+word[0])
        else:
            print('No hint I guess \n')
        guess=input('Enter what you think is the answer.            ')
        if guess==word:
            print('congratulations!!! You got the answer right')
        else:
            print('incorrect word')
            print('The correct word was...........')
            print(word)
    except ValueError:
        print('Invalid input. Only enter numbers from 1-4.')