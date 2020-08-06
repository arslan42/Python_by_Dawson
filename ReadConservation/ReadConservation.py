import pickle,shelve

print("\nUncoservation of lists")
f=open("pickles1.dat","rb")
variety=pickle.load(f)
shape=pickle.load(f)
brand=pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()
