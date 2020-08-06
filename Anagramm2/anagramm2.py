#Anagramm2
import random

WORDS=("python", "anagramm","simple","hard","answer","cup holder")
word=random.choice(WORDS)
correct=word

jumble=""

while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]

print(
"""
    Welcome to game "Anagramm"!
You need to change letter to make word
(For exit press Enter in first session)
"""
)
print("here is anagramm: ",jumble)

guess=input("\ntry to guess the word: ")
while guess!=correct and guess!="":
    print("Sorry, next try")
    guess=input("Try to guess the word: ")

if guess==correct:
    print("That`s right, bro!")

    
print("Thank you for the game")
input("\n\n\Press enter to exit")
