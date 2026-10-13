import sys

class ArgumentError(Exception):
    pass

def main():
    try:
        if len(sys.argv) != 3:
            raise ArgumentError("It needs two parameter")

        x = int(sys.argv[1])
        y = int(sys.argv[2])
    except ArgumentError as Arg:
        print("Error",Arg)
        exit()
    except ValueError as msg:
        print("message error :", msg)
        exit()
    #multiplication
    print(f"{x} times {y} equal {multiplication(x, y)}")
    print("the last one use the while loop to do the same operation")
    print(f"{x} times {y} equal {multiplication_iterate_method(y, x)} \n")
    #power
    print(f"{x} power {y} equal {power_recur(x, y)}")
    print("for this one , I use the Iterative method")
    print(f"{x} power {y} equal {power_iterate(x, y)} \n")
    #factorial
    print(f"{x}! equal {factorial_recur(x)}")
    print(f"{y}! equal {factorial_iterate(y)}")



def multiplication(x:int, y:int) -> int:
    if y == 0 or x == 0:
        return 0
    elif x == 1:
        return y
    else:
        return multiplication(y, x - 1 ) + y

def multiplication_iterate_method(x:int, y:int) -> int:
    result = 0
    if x == 0 or y == 0:
        return 0

    while y > 0:
        result += x
        y -= 1
    return result

def power_recur(n:int, p:int) -> int:
    if p == 0:
        return 1
    else:
        return power_recur(n, p - 1) * n

def power_iterate(n:int, p:int) -> int:
    result = 1
    if p == 0:
        return result

    for i in range(p):
        result *= n
    return result
    
def factorial_recur(n:int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return factorial_recur(n - 1) * n

def factorial_iterate(n:int) -> int:
    result = 1
    if n == 0 or n == 1:
        return 1

    while n > 0:
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    main()
