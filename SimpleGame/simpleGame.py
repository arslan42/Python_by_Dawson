#demonstrate import
import games,random

print("Welcome to simplest game!\n")
again=None
while again!="n":
    players=[]
    num=games.ask_number(question="How much players play? (2-5)",low=2,high=5)
    for i in range(num):
        name=input("Playes name: ")
        score=random.randrange(100)+1
        player=games.Player(name,score)
        players.append(player)

    print("Results of the game")
    for player in players:
        print(player)
    again=games.ask_yes_no("\n Wanna replay? (y/n)")
input("\n\nPress Enter to exit")
