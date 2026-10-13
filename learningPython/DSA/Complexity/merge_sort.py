#it takes n * log(n) :w


def merge_sort(array) -> list:
    if len(array) <= 1:
        return array

    left_half, right_half = split(array)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(array:list)-> tuple:
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    return (left, right)

def merge(left:list, right:list)->list:
    l = []
    i = 0 
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(array:list) -> bool:
    n = len(array)

    if n == 0 or n == 1:
        return True

    return array[0] < array[1] and verify_sorted(array[1:])


alist = [52, 54,95, 85, 21,2]
print(verify_sorted(alist))
print(alist)

l = merge_sort(alist)
print(verify_sorted(l))
print(l)
