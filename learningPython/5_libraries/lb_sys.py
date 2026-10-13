import sys

#sys.exit('str') exit with str like a msg in the console
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#print("hello , my name is" , sys.argv[1]) 

for arg in sys.argv[1:]:
    print("hello , my name is", arg)
    print(type(arg))
