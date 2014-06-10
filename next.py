#!/usr/bin/python3

numbers = [0,1,2,3,4,5,2,4,3,43,43,2,432,3,1]
print numbers[9:14]

numbersx2 = numbers * 2

print numbersx2[0:]

print numbers[:]

with open("test.txt", "wt") as out_file:
    out_file.write("Text!")

import subprocess
def main():
    subprocess.call(['ls', '/'])
main()
