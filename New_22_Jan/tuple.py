"""
@author : Nishant Sanjay Kumbhar
@goal : tuple example
"""
s = "*"
t = ("Nishant", "Sanjay", "Kumbhar")
for i in t:
    print(i)

print(s*20)

l = []
for i in t:
    l.append(i)
print(l)

print(s*20)
# The enumerate() function takes a list as a parameter and returns a tuple for each element in the list.
# The first value of the tuple is the index
# and the second value is the element itself.

t1 = ("Nishant", "Sanjay", "Kumbhar")
for i, j in enumerate(t1):
    print("i : {}  and  j : {}".format(i, j))

print(s*20)

l1 = ["Nishant", "Sanjay", "Kumbhar"]
for i, j in enumerate(l1):
    print("i : {}  and  j : {}".format(i, j))

print(s*20)

t2 = ("Nishant", "Kumbhar")
for i in t2:
    print(i)

print(s*20)

"""
t3 = ("Nishant", "Kumbhar")
for i, j in t3:
    print(i)

l2 = ["Nishant", "Kumbhar"]
for i, j in l2:
    print(i)    

# above are giving error

"""
# see why above program giving error

t4 = (("Nishant", "Kumbhar"), ("Shubham", "Khutale"))
for i, j in t4:
    print("i : {} , j : {}".format(i, j))

print(s*20)

l3 = [("Nishant", "Kumbhar"), ("Shubham", "Khutale")]
for i, j in l3:
    print("i : {} , j : {}".format(i, j))

print(s*20)

l4 = [["Nishant", "Kumbhar"], ["Shubham", "Khutale"]]
for i, j in t4:
    print("i : {} , j : {}".format(i, j))

print(s*20)

master = [("Nishant", "Kumbhar"), ("Shubham", "Khutale"), ("Raj", "Jagtap")]
print(master)
for name, surname in master:
    print("{} is the name and {} is the surname.".format(name, surname))

print(s*20)

"""
for index, name, surname in enumerate(master):
    print("{} : {} is the name and {} is the surname.".format(index, name, surname))
"""
# above also get errors