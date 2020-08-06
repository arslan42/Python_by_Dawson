#demonstrate list`s methods
scores=[]
choice=""

while choice=="":
    print(
        """
Records
0-Exit
1-Help
2-Add record
3-Delete record
4-Sort list
        """
        )
    choice=input("Your choice: ")
    print()
    
exit
if choice=="0":
    print("Good bye!")

#print results
elif choice=="1":
    print("Records")
    for score in scores:
        print(score)
#append result
elif choice=="2":
    score=int(input("Type your record:"))
    scores.append(score)
#delete result
elif choice=="3":
    score=int(input("Which result to delete?: "))
    if score in scores:
        scores.remove(score)
    else:
        print("Result ",score," not in this list")
#sort
elif choice=="4":
    scores.sort(reverse=True)

else:
    print("There is no such number in menu: ",choice)

input("\n\nPress enter to exit")
        
