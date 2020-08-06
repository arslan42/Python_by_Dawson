#demonstrate using of dictionaries
choice=""
while choice=="":
    print(
        """
Translate from geek to english
0-Exit
1-Found translation
2-Add term
3-Change translation
4-Delete term
        """
        )
    choice=input("your choice: ")
    print()
#exit
if choice="0":
    print("Good bye!")

#translate
elif choice=="1":
    term=input("What term you want to translate? ")
    if term in geek:
        definition=geek[term]
        print("\n",term," means ",definition)
    else:
        print("Not such term in dictionary: ", term)
#add term
elif choice=="2":
    term=input("What term do you want to add? ")
    if term not in geek:
        definition=input("\nType your definition: ")
        geek[term]=definiton
        print("\nTerm", term, "added to dictionary")
    else:
        print("\n Such term already exists")
#replace
elif choice=="3":
    term=input("which term do you want to remake?")
    if term in geek:
        definition=input("Type your definition: ")
        geek[term]=definition
        print("\nTerm",term," redefenited")
    else:
        print("No such term in dictionary!")
#delete
elif choice=="4":
    term=input("Which term do want to delete?")
    if term in geek:
        del geek[term]
        print("\nTerm",term,"deleted")
    else:
        print("No such term in dictionary")

        

geek={"404":"Don`t know",
      "Googling":"Search information",
      "Keyboard plague":"Garbage in keyboard",
      "Link Tor":"....",
      "Uninstalled":"Fire somebody"}

print(geek["404"])

if "googling" in geek:
    print("I know what it means")
else:
    print("I don`t know what it means")
print(geek.get("googling","i don`t know"))
print(geek.get("googling"))

print(geek.values())
print(geek.items())
print(geek.keys())
input("\n\nPress enter to exit")
