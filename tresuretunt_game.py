import random
grid=[]
print('WELCOM TO THE TRESURE HUNT GAME!!!')
for i in range (5):
    row=["_","_","_","_","_"]
    grid.append(row)
for i in grid:
    print(''.join(i))
tr=random.randint(0,4)
tc=random.randint(0,4)
while True:
    try:
        row=int(input('Guess the row the tresure is in? (0-4)          '))
        column=int(input('Guess the column the tresure is in? (0-4)          '))
        if row<tr:
            print(f'The row is higher than {row}')
        if row>tr:
            print(f'The row is lower than {row}')
        if column<tc:
            print(f'The column is higher than {column}')
        if column>tc:
            print(f'The column is lower than {column}')
        if row==tr and column==tc:
            print(f'YOU FOUND THE TRESURE!!!')
    except ValueError:
        print("Invalid input")