#demonstrate global vars
def read_global():
    print(" value in read_global=",value)
def shadow_global():
    value=-10
    print("value in shadow_global=",value)
def change_global():
    global value
    value=-10
    print("value in change_global=",value)

#main part
value=10
print("in global value=",value,"\n")
read_global()
print("in global value=",value,"\n")
shadow_global()
print("in global value=",value,"\n")
change_global()
print("in global value=",value,"\n")

input("\n\npress enter to exit")
