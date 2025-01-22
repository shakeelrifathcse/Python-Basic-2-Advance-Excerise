import random

def play():
    user_choice = input(f"Enter your choice :- ('r' for rock,'s' for scissor,'p' for paper) =>")
    computer_choice = random.choice(["r","s","p"])

    if computer_choice == user_choice:
        return('GameDraw!!!')

    if iswin(user_choice,computer_choice):
        return("You won")

    return("You lost")

#r>s;s>p;r>p winning certeria

def iswin(a,b):
    if (a == "r" or b =="s") and (a =="s"or b =="p") and (a =="p" or b =="r"):
        return True
    
print(play())






