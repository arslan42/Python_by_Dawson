#demonstrate indexing of string
import random
word="index"
print("var word contain word: ",word,"\n")
high=len(word)
low=-len(word)
for i in range(10):
    position=random.randrange(low,high)
    print("word[",position,"]\t",word[position])
input("\n\nPress Enter to exit")
