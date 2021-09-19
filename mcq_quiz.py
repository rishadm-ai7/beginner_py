choice=input("Do you want to play?\n1)Yes\n2)No")
if choice =='1':
    print("Welcome to the quiz\n\tGood Luck")
elif choice =='2':
    quit()
else:
        print("Invalid choice,Please try again!")
score=0


#Question 1

answer=input("What is software?\n1)Clothing designed to be worn by computer users\n2)Any part of the computer that has a physical structure\n3)Instructions that tell the hardware what to do")
if answer=='3':
    print("Good Job, Right Answer!")
    score+=1
else:
    print("Wrong Answer")


#Question 2

answer=input("The computer’s main circuit board is called a ________.\n1)Monitor\n2)Motherboard\n3)Hard Drive\n")
if answer=='2':
    print("Good Job, Right Answer!")
    score+=1
else:
    print("Wrong Answer")


#Question 3

answer=input("RAM is like a computer’s ________, while a hard drive is like a computer’s ________.\n1)short-term memory/long-term memory\n2)nervous system/brain\n3)brain/nervous system\n")
if answer=='1':
    print("Good Job, Right Answer!")
    score+=1
else:
    print("Wrong Answer")


#Question 4

answer=input("What is an Ethernet port used for?\n1)Connecting smartphones and other peripherals\n2)Connecting to the Internet\n3)Providing power to the computer\n")
if answer=='2':
    print("Good Job, Right Answer!")
    score+=1
else:
    print("Wrong Answer")


#Question 5

answer=input("Windows, macOS, and Linux are examples of ________.\n1)Internet service providers\n2)web browsers\n3)operating systems\n")
if answer=='3':
    print("Good Job, Right Answer!")
    score+=1
else:
    print("Wrong Answer")

percentage=score*20
print("Congratulations you have finished the quiz, you got " +str (score)+" questions correct")
print("You scored "+str(score*20)+"%")