
def main():
    original_list = [1, 2, 2, 5, 5, 4]

    list_1 = make_list( original_list )
    list_2 = make_list_comprehension( original_list )

    print( f"{list_1} another way with the comprehension {list_2}" )

def make_list(array: list) -> list:
    new_list = []
    for element in array:
        new_list.append(element** 2)
    return new_list

def make_list_comprehension(array: list) -> list:
    return [ element** 2 for element in array ]


if __name__ == "__main__":
    main()
