#in this lesson , I figure out SynthaxeError ValueError NameError
#pass keyword : quit the part of code in the block:wq:
def main():
    x = get_int("what's x ? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not a integer")
        else:    
            return x
    
main()
