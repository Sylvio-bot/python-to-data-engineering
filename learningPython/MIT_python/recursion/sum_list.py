def main():
    array = [ 1, 2, 3]
    print("The total of element inside the array : ",sum_list_rec(array) )

def sum_list_rec(array:list) -> int | float:
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_list_rec(array[1:])

if __name__ == "__main__":
    main()
