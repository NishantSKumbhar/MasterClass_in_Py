l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

it = iter(l1)

print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))
print(it.__next__())
print(next(it))