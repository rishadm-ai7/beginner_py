import random

urange=input("Enter a upper limit: ")
guesses=1
if urange.isdigit():
    urange=int(urange)
    if urange<=0:
        print("Please enter a number greater than 0")
        quit()

else:
    print("Please enter a number: ")
    quit()

randomnumber = random.randint(0,urange)

while True:
    guesses+=1
    guess=input("Make a guess: \n")
    if guess.isdigit():
        guess=int(guess)

    else:
        print("Please enter a number greater than 0 \n")
        continue

    if guess==randomnumber:
        if guesses==1:
            print("you got it right in 1 guess")
            break
        else:
            print("You got it right in",guesses,"guesses")
            break
        
    elif guess>randomnumber:
        print("Guess a lower number")
    else:
        print("guess a higher number")
    
