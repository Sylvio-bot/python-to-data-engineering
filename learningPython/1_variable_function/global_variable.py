x = "awesome"

def main():   
    myfunc()

    print("python is " + x + " language")

def myfunc():
    global x 
    x = "great"

if __name__ == "__main__":
    main()
   
