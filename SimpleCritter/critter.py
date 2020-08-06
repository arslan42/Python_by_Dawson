#demonstrate classes
class Critter(object):
    """Virtual critter"""
    def __init__(self,name):
        print("New creature has shown!")
        self.name=name
    def __str__(self):
        rep="Object of Critter class\n"
        rep+="name: "+self.name+"\n"
        return rep
    def talk(self):
        print("Hi, My name is ",self.name,"\n")

#main part
crit=Critter("Bobby")
crit.talk()
crit1=Critter("Murzi")
crit1.talk()

print("Print object crit: ")
print(crit)
print("Access to crit.name: ")
print(crit.name)

input("\n\nPress Enter to exit")
