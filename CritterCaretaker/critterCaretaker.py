class Critter(object):
    """Virtual pet"""
    def __init__(self,name,hunger=0,boredom=0):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):
        self.hunger+=1
        self.boredom+=1
    @property
    def mood(self):
        unhappiness=self.hunger+self.boredom
        if unhappiness<5:
            m="fine"
        elif 5<=unhappiness<=10:
            m="not bat"
        elif 11<=unhappiness<=15:
            m="not so good"
        else:
            m="bad"
        return m

    def talk(self):
        print("My nane is ", self.name,", and i feel ",self.mood," now\n")
        self.__pass_time()

    def eat(self,food=4):
        print("Mrrr..thanx!")
        self.hunger-=food
        if self.hunger<0:
            self.hunger=0
        self.__pass_time()

    def play(self,fun=4):
        print("UWEE")
        self.boredom-=fun
        if self.boredom<0:
            self.boredom=0
        self.__pass_time()

def main():
        crit_name=input("How would you name your pet?")
        crit=Critter(crit_name)
        choice=None
        while choice!="0":
            print(
            """
            My PET
            0-exit
            1-Explore condition
            2-Feed pet
            3-Play with pet
            """
            )
            choice=input("Your choice: ")
            print()
            #exit
            if choice=="0":
                print("Goodbye")
            #talk with pets
            elif choice=="1":
                crit.talk()
            elif choice=="2":
                crit.eat()
            elif choice=="3":
                crit.play()
            #uknown nInput
            else:
                print("Sorry, uknown input: ", choice)



main()
input("\n\nPress enter to exit")
