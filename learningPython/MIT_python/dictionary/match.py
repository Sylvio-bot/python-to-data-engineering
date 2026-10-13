def main():
    d = {1:2, 3:4, 5:6}
    print(count_matches(d)) # print 0
    d = {1:2, 'a':'a', 5:5} # pirnt 2
    print(count_matches(d))

def count_matches(d:dict) -> int:
    """
       return how many entries in d have the key equal to its value
    """
    count = 0
    for key,value in d.items():
        print(f"key : {key} and value {value}")
        if key == value:
            count += 1
    return count

if __name__ == "__main__":
    main()
