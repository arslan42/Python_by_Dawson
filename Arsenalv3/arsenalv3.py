#demonstrate lists
inventory=["sword","armor","shield","hil potion"]
print("\nSo, your arsenal: ")
for item in inventory:
    print(item)
print("In your arsenal ",len(inventory)," things")

if "hil potion" in inventory:
    print("Long life to the King!")

#slice
start=int(input("\nPut start index: "))
finish=int(input("\nPut end index: "))
print("Slise of inventory[",start,":",finish,"] - ",end=" ")
print(inventory[start:finish])
print(inventory[3])
print(inventory[0])

#concatenation
chest=["gold","brilliants"]
print("You have found chest, there are: ")
print(chest)
print("You added chest your to arsenal")
inventory+=chest
print("Here in your arsenal: ")
print(inventory)

#change list
print("You change sword to arbalest")
inventory[0]="arbalest"
print("Here in your arsenal: ")
print(inventory)

#slice
print("We bought magic crystal for gold and brilliants, that can see the future")
inventory[4:6]=["magic crystal"]
print("Here in your arsenal: ")
print(inventory)

#deleting
print("Shield was broken")
del inventory[2]
print("Here in your arsenal: ")
print(inventory)

#deleting slice
del inventory[:2]
print("Thiefs taked arbalest and armor")
print("Here in your arsenal: ")
print(inventory)


input ("\nPress enter to exit")
