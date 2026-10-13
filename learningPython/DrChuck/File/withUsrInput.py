"""
  it's possible the file doesn't exist so
  the open method return a error
"""

give_fileName = input("Enter the file name: ")
try:
    file = open(give_fileName)
except:
    print("File cannot be opend :",give_fileName)
    exit()

for line in file:
    line = line.rstrip()
    print(line)
