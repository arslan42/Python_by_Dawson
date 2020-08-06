#demonstrate predicats
print("\tExclusive computer network")
print("\t only for registered users\n")
security=0
username=""
while not username:
    username=input("Login: ")
password=""
while not password:
    password=input("Password: ")
if username=="M.Dawson" and password=="secret":
    print("Hi, Mike")
    security=5
elif username=="S.Meier" and password=="civilization":
    print("Hi, Sid")
    security=3
elif username=="S.Miyamoto" and password=="mariobros":
    print ("Hi, Sigeru")
    security=3
elif username=="W.Wright" and password=="thesims":
    print("How are you, Will?")
    security=3
elif username=="guest" or password=="guest":
    print("Welcome guest")
    security=1
else:
    print("No access\n")
input("\n\nPush Enter to exit")
