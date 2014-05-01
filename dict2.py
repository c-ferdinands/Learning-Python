numbers = {}
print("Add Name and Number")
name = input("Name: ")
phone = input("Number: ")
numbers[name] = phone
for x in numbers.keys():
    print("Name: ", x, "\tNumber:", numbers[x])

