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


def print_options():
    print("Options:")
    print(" 'p' print options")
    print(" 'c' convert from Celsius")
    print(" 'f' convert from Fahrenheit")
    print(" 'q' quit the program")
 
def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32
 
def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0
def menu():
    choice = "p"
    while choice != "q":
        if choice == "c":
            c_temp = float(input("Celsius temperature: "))
            print("Fahrenheit:", celsius_to_fahrenheit(c_temp))
            choice = input("option: ")
        elif choice == "f":
            f_temp = float(input("Fahrenheit temperature: "))
            print("Celsius:", fahrenheit_to_celsius(f_temp))
            choice = input("option: ")
        elif choice == "p": #Alternatively choice != "q": so that print when anything unexpected inputed
            print_options()
            choice = input("option: ")
        elif choice != "q":
            print("Pick a Choice! - Fuckwit")
            print_options()
            choice = input("option: ")
        elif choice == "q":
            choice = q
    print("Die")

menu()
