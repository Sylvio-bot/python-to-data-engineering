def main():
    array = [1, 2 , 2, 2, 5]
    remove_all( array, 2 )
    print(array)

def remove_all(array:list, element:int) -> list:
    while element in array:
        array.remove(element)
        

if __name__ == "__main__":
    main()

