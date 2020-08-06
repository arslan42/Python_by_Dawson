#demonstrate kortej creation
inventory=()
if not inventory:
    print("you have no weapeon")
input("\nPress Enter to continiue")
inventory=("sword",
           "armor",
           "shield",
           "hil potion")

print("\nKortej contains:")
print(inventory)
print("\nSo, in your arsenal:")
for item in inventory:
    print(item)
input("\n\nPress ENter to exit")
