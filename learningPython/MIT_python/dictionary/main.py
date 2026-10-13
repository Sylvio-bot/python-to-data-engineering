
def main(): 
    d1 = {1:2, 3:4, 5:6}
    d2 = {2:4, 4:6}
    d3 = {1:1, 3:9, 4:16, 5:25}
    
    print(find_in_L([d1, d2, d3], 2)) # returns True
    print(find_in_L([d1, d2, d3], 25)) # returns False

def find_in_L(Ld:list[dict], k:int) -> bool:
    for elem_dict in Ld:
        if k in elem_dict:
            return True
        
    return False

if __name__ == "__main__":
    main()

