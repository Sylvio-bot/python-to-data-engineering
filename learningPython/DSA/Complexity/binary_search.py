'''
  Known variable
    start_index , end_index, middle_index , target
  setp one:
     compare the content in the middle and the target
         if greater than
            start_index = middle + 1
         else if less than
            end_index = middle - 1
         else equal
            retun index

  Do this step one until start_index is less than or equal end_index

  setp two:
     we verify if the first setp return a index or None
     verify(setp one) = (None)? it finds : it does'nt find)
'''
def main():
    target = int(input("Enter your target number "))
    result = binary_search([i for i in range(1,11)], target)
    print(verify(result) )

def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1
    
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if array[middle_index] > target:
            end_index = middle_index - 1
        elif array[middle_index] < target:
            start_index = middle_index + 1
        else:
            return middle_index
        
    return None

def verify(index):
    return f"it finds {index}" if index is not None else "it doesn't find"

if __name__ == "__main__":
    main()

