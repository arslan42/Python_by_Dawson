import pickle,shelve

print("\n Put lists on shelve")
s=shelve.open("pickles2.dat")

s["variety"]=["ogurci","pomidori","kapusta"]
s["shape"]=["entirely","cubs","strips"]
s["brand"]=["GlavProduct","Chumak","Bondwell"]

s.sync()

print("\nTaking lists from shelve")
print("brands: ",s["brand"])
print("forms",s["shape"])
print("kinds of vegetables",s["variety"])

s.close()
input("\n\nPRess Enter to exit")
