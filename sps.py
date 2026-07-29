import random
computer=random.choice([-1,0,1])
options={"stone":1,"paper":0,"scissor":-1}
you=input("Enter your choice:")
you=options[you.lower()]
revdict= {-1:"scissor", 0:"paper", 1:"stone"}
print(f"YOUR CHOICE = {revdict[you]}\nCOMPUTER CHOICE = {revdict[computer]}")
if computer==you:
    print("DRAWN")

else:
    if computer == -1 and you == 1:
        print("you won!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 0 and you == 1:
        print("You lose!")
    elif computer == 0 and you == -1:
        print("you win!")      
    elif computer == 1 and you == 0:
        print("You win ")
    elif computer == 1 and you == -1:
        print("You lose!")
    else:
        print("Something went wrong!")
        