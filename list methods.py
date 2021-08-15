#List methods

#append()
x=["apple","orange","banana"]
x.append("papaya")
print(x)

#clear()
x=["BMW","benze","audi","Maruthi"]
x.clear()
print(x)

#copy()
x=["xyz","iuyr","skhf"]
print(x.copy())

#count()
z=["2","5","6","5","9","5"]
y=z.count("5")
print(y)

#extend()
x=["bugati","bmw"]
y=["maruthi","toyoto"]
x.extend(y)
print(x)

#index()
l1=["spaceX","5","bmw"]
print(l1.index("bmw"))

#insert()
l2=["papaya","5","bmw"]
l2.insert(1,"tesla")
print(l2)

#pop()
l2=["papaya","5","bmw"]
l2.pop()
print(l2)

#remove()
l3=["bmw","5","33","bugati"]
l3.remove("33")
print(l3)

#reverse()
x=["bmw","5","33","bugati"]
x.reverse()
print(x)

#sort()
l4=["demo","audi","css","z"]
l4.sort()
print(l4)
