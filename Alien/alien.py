#demonstrate objects actions
class Player(object):
    """Player in action game"""
    def blast(self,enemy):
        print("Player shoot down the enemy\n")
        enemy.die()
class Alien(object):
    """Evil alien in action game"""
    def die(self):
        print("That`s all...asta la vista baby")
        print("goodbye, cruel world")

#main part
print("\t\tALien`s death")
hero=Player()
invader=Alien()
hero.blast(invader)
input("\n\nPress ENter to exit")
