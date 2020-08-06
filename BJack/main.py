import games,cards,bjack
#main part
def main():
 print("\t\tWelcome to BJack game table!\n")
 names=[]
 number=games.ask_number("How much player?(1-7):",low=1,high=8)
 for i in range(number):
    name=input("Type players name: ")
    names.append(name)
    print()
 game=bjack.BJ_Game(names)
 again=None
 while again!="n":
    game.play()
    again=games.ask_yes_no("\nWanna replay?")
    main()
 input("\n\nPress Enter to exit")

main()
