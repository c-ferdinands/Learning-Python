#!/usr/bin/python3

onetoten = range(1, 11)
for item in onetoten:
    print(item)

list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
list.sort()
print(list)
prev = None
for item in list:
    if prev == item:
        print("Duplicate of", prev, "found")
        print("Removing", prev)
        list.remove(prev)
    prev = item
print(list)
