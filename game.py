import random
choices=["rock","paper","scissor"]
user=input("enter your choice rock, paper or scissor: ")
computer=random.choice(choices)
print("computer choice is ",computer)
print("user choice is ",user)
if user==computer:
    print("its a tie")
elif(user=="rock" and computer=="scissor") or (user=="paper" and computer=="rock") or (user=="scissor" and computer=="paper"):
    print("you win")
else:
    print("computer wins")