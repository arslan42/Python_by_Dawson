import random

print("\tWelcome to the game 'Guess the number'1")
print("\nI made a guess natural number in 1 to 100")
print("Try to guess it in minimal tries")

the_number=random.randint(1,100)
guess=int(input("Your choice:"))
tries=1
while guess!=the_number:
    if guess>the_number:
        print("lower")
    else:
        print("higher")
    guess=int(input("Your choice:"))
    tries+=1
print("Congratulations! It`s ", the_number)
print("Number of tries ",tries)
