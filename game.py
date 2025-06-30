#stone paper scissors game coded by Ayush Goswami 
import random
k=["stone","paper","scissors"]
you=0
computer=0
print("welcome to the stone , paper , scissors game.....")
while True:
    user_input=input("enter your choice stone , paper , scissors:").lower()
    com_choice=random.choice(k)
    print("computer's choice is:",com_choice)
    if user_input not in k:
        print("your choice is incorrect")
    elif user_input==com_choice:
        print("it's a tie")
    elif (user_input=="stone" and com_choice=="scissors") or (user_input=="paper" and com_choice=="stone" ) or (user_input=="scissors" and com_choice=="paper"): 
        print("hurray! you won the match")
        you=you+1
    else:
         print("you loose the match")
         computer = computer+1
    print(f" you :{you} || computer: {computer}")
    again=input("do you wants to exit yes/no:")
    if again=="yes":
        print(f" finall score is you :{you} || computer: {computer}")
        print("I enjoyed to play with you goodbye!!")
        break
    