#!/usr/bin/python3

# password = str()
# while password != "unicorn":
#     password = input("Password: ")
# print("Continues...")
# 
# print("Halt!")
# user_input = input("What is your name? ")
# user_input2 = input("What is your Age? ")
# print("You may pass,",  user_input, "because you are", user_input2)
# 
# 
# ""
# a = 1
# s = 0
# print('Enter Numbers to add to the sum.')
# print('Enter 0 to quit.')
# while a != 0:
#     print('Current Sum:', s)
#     a = float(input('Number? '))
#     s = s + a
# ""
# 
# b = 0
# c = 0
# while c < 10:
#     c = c + 1
#     print(user_input2)
# 
# name = input('Set name: ')
# password = input('Set password: ')
# while 1 == 1:
#     nameguess=""
#     passwordguess=""
#     key=""
#     while (nameguess != name) or (passwordguess != password):
#         nameguess = input('Name? ')
#         passwordguess = input('Password? ')
#     print("Welcome,", name, ". Type lock to lock.")
#     while key != "lock":
#         key = input("")
# 
# int = 1
# while int == 1:
#     name = input('Your name: ')
#     if name == 'John1':
#         print('That is a nice name.')
#     elif name == 'Jim':
#         print('... some funny text.')
#     elif name == 'John':
#         print('... some funny text.')
#     elif name == 'Die':
#         int = input('Set 0 to die ')
#     else:
#         print('You have a nice name.')
#

 
''' 
pings
Small program to check input for 5x! otherwise fail, invalid input returns 'Fuckwit' and dies 
'''
#def ping():
#    int = 0
#    while int == 0:
#        ping = input('Pings?: ')
#        if ping == '!!!!!':
#           print('Success!')
#        elif ping == '.....':
#           print('Fail')
#        else:
#           print('Fuckwit')
#           int = 1
#ping()

'''
Variables
'''

#def print_options():
#    print("Options:")
#    print(" 'p' print options")
#    print(" 'c' convert from Celsius")
#    print(" 'f' convert from Fahrenheit")
#    print(" 'q' quit the program")
# 
#def celsius_to_fahrenheit(c_temp):
#    return 9.0 / 5.0 * c_temp + 32
# 
#def fahrenheit_to_celsius(f_temp):
#    return (f_temp - 32.0) * 5.0 / 9.0
#def menu(choice):
#    while choice != "q":
#        if choice == "c":
#            c_temp = float(input("Celsius temperature: "))
#            print("Fahrenheit:", celsius_to_fahrenheit(c_temp))
#            choice = input("option: ")
#        elif choice == "f":
#            f_temp = float(input("Fahrenheit temperature: "))
#            print("Celsius:", fahrenheit_to_celsius(f_temp))
#            choice = input("option: ")
#        elif choice == "p": #Alternatively choice != "q": so that print when anything unexpected inputed
#            print_options()
#            choice = input("option: ")
#        elif choice != "q":
#            print("Pick a Choice! - Fuckwit")
#            print_options()
#            choice = input("option: ")
#        elif choice == "q":
#            choice = q
#    print("Die")
#
#menu("p")
# numbers = {}
# print("Add Name and Number")
# name = input("Name: ")
# phone = input("Number: ")
# numbers[name] = phone
# for x in numbers.keys():
#     print("Name: ", x, "\tNumber:", numbers[x])
# 
# fucks = {}
# 
# who = input("Who gives the fucks?? ")
# given = input("How many?? ")
# fucks[who] = given
# for x in fucks.keys():
#      print(x, "give", fucks[x], "fucks")
# fucks = {}
# 
# who = input("Who is giving the fucks? ")
# given = input("how many fucks are given? ")
# fucks[who] = given
# for x in fucks.keys():
#     print(x, "give", fucks[x], "fucks")
# 
#!/usr/bin/python3

#which_one = int(input("What month (1-12)? "))
#months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#          'August', 'September', 'October', 'November', 'December'] 
#if 1 <= which_one <= 12:
#    print("The month is", months[which_one - 1]
#print('Die')



#def guess_month():
#    which_one = int(input("What month (1-12)? "))
#    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#              'August', 'September', 'October', 'November', 'December']
#    if 1 <= which_one <= 12:
#        print("The month is", months[which_one - 1])
#    else:
#        print("Enter 1-12")
#while 1 == 1:
#    guess_month()

# menu_item=0
# namelist = []
# while menu_item != 9:
#     print("......")
#     print("1. Print List")
#     print("2. Add to List")
#     print("3. Remove from list")
#     print("4. Change item in list")
#     print("9. die")
# 
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
fucks = {}
who = input("Who is giving the fucks? ")
given = input("how many fucks are given? ")
fucks[who] = given
for x in fucks.keys():
    print(who, "\tgives", given, "fucks")

 
# numbers = {}
# print("Add Name and Number")
# name = input("Name: ")
# phone = input("Number: ")
# numbers[name] = phone
# for x in numbers.keys():
#     print("Name: ", x, "\tNumber:", numbers[x])
#
#






















from time import time, ctime
print(ctime(time()))



