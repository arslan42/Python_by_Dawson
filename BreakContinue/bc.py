#demonstrate break and continiue
count=0
while True:
    count+=1
    if count>10:
        break
    if count==5:
        continue
    print(count)
input("\n\nPush Enter to exit")
