def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f'hello, {name}')

def goodbye(name):
    print(f"goodbye, {name}")

#__name__ is a special variable which equal a modul in the other file
if __name__ == "__main__":
    main()
