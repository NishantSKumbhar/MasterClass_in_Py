l = ['Apple', 'Banana', 'Mango', 'Strawberry', 89, False, 45.56]

print(l)

l.insert(1, 'Iphone 13')

print(l)

last = l.pop()

print(last)
print(l)

l.remove('Banana')
print(l)

l.clear()

print(l)

l = ['Apple', 'Banana', 'Mango', 'Strawberry', 89, False, 45.56]

print(l)

l.reverse()
print(l)

#l.sort() for numbers

l1 = [32, 4,67, 5, 343, 67, 908]

new_list = sorted(l1)
print(new_list)


l2 = [0] * 5
print(l2)

my_list = l1 + l2

print(my_list)

new = sorted(l1+l2)
print(new)

l=[1,2, 3,4, 5,6, 7, 8, 9, 10, 11, 12]
a = l[1:5]
print(a)

b = l[:5]
print(b)

c =l[1:]
print(c)

d = l[::1]
print(f"d: {d}")

e = l[::2]
print(e)

r = l[::-1]
print(f"r:{r}")

k = l
print(k)
k.pop()
print(k)
print(l)

m = l.copy()
# or m = list(l)
# or m = l[:]
m.pop()

print(m)
print(l)