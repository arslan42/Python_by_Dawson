#demonstrate hot to create new strings from originals with circle for
message=input("Input the text: ")
new_message=""
VOWELS="afhdsjfhskfs"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message+=letter
        print("Created new string: ", new_message)
print("\nHere`s your text without glasnii letters:", new_message)
input("\n\nPush enter to exit")
