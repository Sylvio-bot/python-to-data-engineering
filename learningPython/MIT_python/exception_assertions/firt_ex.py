try:
    a = int(input("Tell mes one number: "))
    b = int(input("Tell me another number: "))

    print(f"{a} divide by {b} equal", a/b)
    print(f"{a} plus {b} equal", a + b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
    print(f"{a} / {b} = INFINITY")
