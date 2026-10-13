def linear_search(list_array, target):
    for i in range(0, len(list_array)):
        if list_array[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("It found in the index", index)
    else:
        print("It doesn't find")


number = [  i  for i in range(1, 11) ]

target = int(input("what's the number? "))
result = linear_search(number, target)
verify(result)
