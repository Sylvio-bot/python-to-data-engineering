import copy

def main():
    old_list = [[1,2],[3,5]]
    new_list = copy.deepcopy(old_list)#copy.copy(old_list) # this is a shallow copy


    #if the list content the immutable and you try changing any list ,it reset all list
    old_list[0][1] = 10
    print(f"the new_list become {new_list} ")
    new_list[0][0] = 5
    print(f"the old_list become {new_list} ")
    
    #if you append a new element
    old_list.append(4)
    print(f"I append a new element in old_list {old_list} new_list {new_list}")

if __name__ == "__main__":
    main()
