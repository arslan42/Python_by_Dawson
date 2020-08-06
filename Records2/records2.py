#Record v2.0
#Demonstrate nested sequences
scores=[]
choice=""
while choice=="":
    print(
        """
Record 2.0
0- Exit
1- Show records
2- Append record
        """
        )
    choice=input("Your choice: ")
    print()
#exit
    if choice=="0":
        print("Good bye!")
#show table of records
    elif choice=="1":
        print("Records \n")
        print("NAME\tRESULT")
        for entry in scores:
            score,name=entry
            print(name,"\t",score)
#add a score
    elif choice=="2":
        name=input("Input player`s name: ")
        score=int(input("Input his result: "))
        entry=(score,name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores=scores[:5]
#wrong choice
    else:
        print("Sorry, no such number in menu",choice)
input("\n\nPress enter to exit")
