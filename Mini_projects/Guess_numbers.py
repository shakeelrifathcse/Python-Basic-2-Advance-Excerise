import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0 
    while guess != random_num:
        guess = int(input(f"Guess the number bw 1 and {x}:"))
        if guess < random_num:
            print("omg...its too low...try again")
        elif guess > random_num:
            print(f"omg...{guess} fucking high....try lesser ")
        else:
            print("Hurray,Congratulations ✅")

guess(10)
    