#game hangman
import random

#const
HANGMAN=(
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    """,
    """
    -----
    |   |
    |   0 |
    |
    |
    |
    |
    |
    """,
    """
    -----
    |   |
    |   0 | +
    |
    |
    |
    |
    |
    """,
    """
    -----
    |   |
    |   0 | /+
    |
    |
    |
    |
    |
    """,
    """
    -----
    |   |
    |   0 | /+/
    |
    |
    |
    |
    |
    """,
    """
    -----
    |   |
    |   0 | /+/
    |   |
    |
    |
    |
    |
    """,
    """
    -----
    |   |
    |   0 | /+/
    |   |
    |   |
    |
    |
    |
    """,
    """
    -----
    |   |
    |   0 | /+/
    |   |
    |   |
    |  |
    |  |
    |
    """,
    """
    -----
    |   |
    |   0 | /+/
    |   |
    |   |
    |  | |
    |  | |
    |
    """)

MAX_WRONG=len(HANGMAN)-1

WORDS=("OVERUSED","CLAM","GUAM","TAFFETA","PYTHON")

#initialization of vars
word=random.choice(WORDS) #word for guessing

so_far="-"*len(word)

wrong=0 #count of mistakes
used=[] #used letters

print("WElcome to game Hangman! Good luck!")
while wrong<MAX_WRONG and so_far!=word:
    print(HANGMAN[wrong])
    print("\nYou already used this letters: \n",used)
    print("\nGuessed looks like:\n",so_far)
    guess=input("\n\nType the letter: ")
    guess=guess.upper()
    while guess in used:
        print("You already typed this letter ", guess)
        guess=input("\n\nType the letter: ")
        guess.upeer()
    used.append(guess)
    if guess in word:
        print("\nYEAH! Letter ",guess," is in the word!")
        #new stroke so_far with guessed letter or letters
        new=""
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far=new
    else:
        print("Unfortunately, there is no such letter ", guess," in the word")
        wrong+=1
if wrong==MAX_WRONG:
    print(HANGMAN[wrong])
    print("\n You were hanged")
else:
    print("\nCongrats!")

print("\n word was -",word)
input("\n\nPress enter to exit")
    
    




    
