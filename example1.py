#!/usr/bin/python3

#onetoten = range(1, 11)
#for item in onetoten:
#    print(item)
#
#list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
#list.sort()	
#print(list)
#prev = None
#for item in list:
#    if prev == item:
#        print("Duplicate of", prev, "found")
#        print("Removing", prev)
#        list.remove(prev)
#    prev = item
#print(len(list))
#
#print(prev >= 10)



#for value in attendees:
#    print(value)


# def genders():
#     attendees = ['Male', 'Female', 'Female', 'Male']
#     male_count = 0
#     female_count = 0
#     current_count = 0
#     while current_count < len(attendees):
#         for value in attendees:
#             if value == 'Male':
#                 male_count = male_count + 1
#                 current_count = current_count + 1
#             else:
#                 female_count = female_count + 1
#                 current_count = current_count + 1
#     else:
#         print("Males:", male_count)
#         print("Females:", female_count)
# genders()

#attendees = ['Male', 'Female', 'Female', 'Male']
#
#print(attendees[1])

# name = raw_input("What is your name? ")
# password = raw_input("What is the password? ")
# if name == "Josh" and password == "Friday":
#     print("Welcome Josh")
# elif name == "Fred" and password == "Rock":
#     print("Welcome Fred")
# else:
#     print("I don't know you.")
#numbers = {}
#print("Add Name and Number")
#name = input("Name: ")
#phone = input("Number: ")
#numbers[name] = phone
#for x in numbers.keys():
#    print("Name: ", x, "\tNumber:", numbers[x])
#
#
#       # print("Add Name and Number")
#       # name = input("Name: ")
#       # phone = input("Number: ")
#       # numbers[name] = phone
#
#
#fucks = {}
#who = input("Who is giving the fucks? ")
#given = input("how many fucks are given? ")
#fucks[who] = given
#for x in fucks.keys():
#    print(who, "\tgives", given, "fucks")


numbers = {}
print("Add Name and Number")
name = input("Name: ")
phone = input("Number: ")
numbers[name] = phone
for x in numbers.keys():
    print("Name: ", x, "\tNumber:", numbers[x])
