#demonstrate conservation data and access throw interface
import pickle,shelve

print("COnservation of list")
variety=["ogurci","pomidori","kapusta"]
shape=['entirely','cubs','strips']
brand=['GlavProduct','Chumak','Bondwell']
f=open("pickles1.dat","wb")

pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()
