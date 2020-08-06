#demonstrate handling exceptions
try:
    num=float(input("Type the number:"))
except ValueError:
    print("Seems like not a number!")

#handling different kinds of exceptions
print()
for value in (None,"Hello!"):
    try:
        print("Trying transform into the the number:",value,"-->",end="")
        print(float(value))
    except(TypeError,ValueError):
        print("Seems like a not a number!")

#
print()
for value in(None,"Hello!"):
    try:
        print("Trying transform into the number: ",value,"-->",endl="")
        print(float(value))
    except TypeError:
        print("I can transform only strings and numbers")
    except ValueError:
        print("I can tranform only strings, contains numbers!")

#taking argument
try:
    num=float(input("\nInput the number: "))
except ValueError as e:
    print("It`s not a number! Interpreter tell us: ")
    print(e)

#+else
try:
    num=float(input("\nInput the number: "))
except ValueError:
    print("It`s not a number!")
else:
    print("You entered number: ",num)
input("\n\nPress Enter to exit")
