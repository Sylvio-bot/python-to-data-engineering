def main():
    print(is_pal(list('abba')))

def is_pal(x:list) -> bool:
    temp = x.copy()
    temp.reverse()
    return temp == x;

if __name__ == "__main__":
    main()
