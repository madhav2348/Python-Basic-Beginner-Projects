import random

options =["rock","paper","scissor"]
user = input("enter your choice \n  rock \n paper \n scissor \n exit")
comp = random.choice(options)
comp_points =0
usr_point=0
if user =="exit":
    print("game over")
    print("you won",usr_point, "and computer wons", comp_points,"points")
    exit = True

if user == "rock":
    if comp =="rock":
        print("your input is rock")
        print("computer is rock")
        print("tie")
    elif comp =="paper":
        print("your input is rock")
        print("computer is paper")
        print("computer win")
        comp_points+=1
    elif comp =="scissor":
        print("your input is rock")
        print("computer is paper")
        print("user wins")
        usr_point+=1

elif user =="paper":
    if comp =="rock":
        print("your input is paper")
        print("computer is rock")
        print("you win")
        usr_point+=1
    elif comp =="paper":
        print("your input is paper")
        print("computer is paper")
        print("its a tie")
        
    elif comp =="scissor":
        print("your input is paper")
        print("computer is paper")
        print("computer wins")
        comp_points+=1

elif user =="scissor":
    if comp =="rock":
        print("your input is scissor")
        print("computer is rock")
        print("computer win")
        comp_points+=1
    elif comp =="paper":
        print("your input is scissor")
        print("computer is paper")
        print("user wins")
        usr_point+=1
        
    elif comp =="scissor":
        print("your input is scissor")
        print("computer is paper")
        print("its  a tie")

elif user != "rock" or "paper" or "scissor":
    print("invalid input")


