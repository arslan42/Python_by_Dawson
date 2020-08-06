#demonstrate slice of strings
word="pizza"


print(word[:])

print(
"""
0  1  2  3  4  5
+--+--+--+--+--+
| p| i| z| z| a|
+--+--+--+--+--+
-5-4 -3 -2 -1
"""
)
print("Enter start and end index for slice 'pizza' which you want")
print("Press Enter to exit, not enter start index")
start=None
while start!="":
    start=(input("\nStart index: "))
    if start:
        start=int(start)
        finish=int(input("End index: "))
        print("Slice word[",start,":",finish,"] looks like",end=" ")
        print(word[start:finish])
input("\n\nPress enter to exit")
      
    
