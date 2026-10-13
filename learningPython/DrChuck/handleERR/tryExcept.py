x = input('Enter a number: ')

try:
    ival = int(x)
except:
    ival = -1

if ival > 0:
    print('Nice Work')
else:
    print('not a number')
