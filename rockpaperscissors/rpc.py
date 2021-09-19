import random as r
computer_wins=0
user_wins=0
options=['rock','paper','scissors','quit']

while True:
    user_pick=input("Enter a choice \n1)Rock\n2)Paper\n3)Scissors\n4)Quit").lower()
    computer_pick=options[r.randint(0,2)]
    if user_pick=='quit':
        break
    elif user_pick not in options:
        break
    
    elif user_pick=='rock' and computer_pick=='scissors':
        user_wins+=1
        print("You Won!")

    elif user_pick=='paper' and computer_pick=='rock':
        user_wins+=1
        print("You Won!")

    elif user_pick=='scissors' and computer_pick=='paper':
        user_wins+=1
        print("You Won!")

    else:
        print("You Lost!")
        computer_wins+=1

print("You won ",user_wins," times")
print("Computer won ",computer_wins," times")