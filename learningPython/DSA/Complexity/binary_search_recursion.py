def main():
    target = int(input("Enter your target number "))
    result = binary_search([i for i in range(1,11)], target)
    print(verify(result) )

def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1
    
    if len(array) > 0:
        middle_index = (start_index + end_index) // 2
        if array[middle_index] > target:
            return binary_search(array[:middle_index], target)
        elif array[middle_index] < target:
            return binary_search(array[(middle_index + 1):], target)
        else:
            return middle_index
        
    return None

def verify(index):
    return f"it finds {index}" if index is not None else "it doesn't find"

if __name__ == "__main__":
    main()

