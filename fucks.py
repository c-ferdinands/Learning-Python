def fucks():
    fucks = {}
    who = input("Who is giving the fucks? ")
    given = input("how many fucks are given? ")
    fucks[who] = given
    for x in fucks.keys():
        print(who, "gives", given, "fucks")
fucks()
