#kortej2
inventory=("sword",
           "armor",
           "shield",
           "hil potion")
print("\SO, in your arsenal:")
for item in inventory:
    print(item)
input("\nPress Enter to continue")
print("Now in your arsenal ",len(inventory)," things")
input("\nPress enter to continiue")

#'in"
if "hil potion" in inventory:
      print("Long life to the King!")

#indexing
index=int(input("\nPut index of thing from arsenal: "))
print("After index ",index," in arsenal is ",inventory[index])

#slice
start=int(input("\nPut start index for slice: "))
finish=int(input("\nPut ending index for slice: "))
print("Slice of inventory [",start,":",finish,"] - it", end=" ")
print(inventory[start:finish])
input("\nPress enter for continiue")

#concatenation
chest=("gold","brilliants")
print("you have found chest. There are: ")
print(chest)
print("You add chest to your arsenal")
inventory+=chest
print("Now in your arsenal: ")
print(inventory)
input("\n\n\Press enter to exit")
