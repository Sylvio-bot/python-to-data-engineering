def main():
    L = [1, 2, 2, 2]
    remove_all( L, 2 ) 
    print(L)

def remove_all(array:list, element:int):
    Lnew = array[:]
    array.clear()

    for n in Lnew:
        if n != element:
            array.append(n)

if __name__ == "__main__":
    main()


