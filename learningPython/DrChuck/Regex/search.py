import re

hand = open("lesson.txt")
number_line = 1
regex = input("what is the pattern? ")
for line  in hand:
    line = line.rstrip()
    if re.search(regex ,line):
        print(number_line ,line , sep=":")
    number_line += 1

