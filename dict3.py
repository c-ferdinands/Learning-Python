fucks = {}

who = input("Who is giving the fucks? ")
given = input("how many fucks are given? ")
fucks[who] = given
for x in fucks.keys():
    print(x, "give", fucks[x], "fucks")

