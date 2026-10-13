import time

def main():
    tstart = time.time()
    c_to_f(24)
    dt = time.time() - tstart
    print(dt, "s, ")

def c_to_f(c:int | float) -> int | float:
    return c*9.0/5 + 32

if __name__ == "__main__":
    main()
