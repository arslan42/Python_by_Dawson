#demonstrate properties
class Critter(object):
    """Virtual pet"""
    def __init__(self,name):
        print("New pet has shown up!")
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        if new_name=="":
            print("Name of pet cannot be null")
        else:
            self.__name=new_name
            print("Name has changed succesfully")
    def talk(self):
        print("\nHI, my name is", self.name)

#main part
crit=Critter("Bobby")
crit.talk()
print("\nPet`s name is ",end=" ")
print(crit.name)
crit.name="Mursi"
print(crit.name)
