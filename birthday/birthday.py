#demonstrate named args and parameters by default
def birthday(name,age):
    print("Happy Birthday,",name,"!"," It`s ",age,". dontcha?\n")
def birthday2(name="camrade Ivanov", age=1):
    print("Happy Birthday,",name,"!"," It`s ",age,". dontcha?\n")
birthday("camrade Ivanov",1)
birthday(1,"camrade Ivanov")
birthday(age=1,name="camrade Ivanov")
birthday2()
birthday2(name="Kate")
birthday2(age=12)
birthday2(name="KAte",age=12)
birthday2("Kate",12)
input("\n\npress enter to exit")
