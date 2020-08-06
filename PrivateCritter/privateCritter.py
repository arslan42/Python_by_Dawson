#demonstrate private vars and methods
class Critter(object):
    """VIrtual pet"""
    def __init__(self,name,mood):
        print("New pet has shown up!")
        self.name=name #open attr
        self.__mood=mood #private attr
    def talk(self):
        print("\nMy name is ",self.name)
        print("I feel ",self.__mood," myself\n")
    def __private_method(self):
        print("THis is private method")
    def public_method(self):
        print("THis is public method")
        self.__private_method()

crit=Critter("BObby","good")
print(crit._Critter__mood)
crit.public_method()
crit._Critter__private_method()
