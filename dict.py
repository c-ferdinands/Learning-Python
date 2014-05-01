fucks = {}

who = input("Who gives the fucks?? ")
given = input("How many?? ")
fucks[who] = given
for x in fucks.keys():
     print(x, "give", fucks[x], "fucks")
