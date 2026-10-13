def main():
    global NEW_LINE
    while True:
         if  NEW_LINE is not None :
             print_column(3)
             break
         NEW_LINE = choice()

def print_column(height):
    print(f"#{NEW_LINE}" * height  )

def choice():
    share = input("Are you need a vertical or horizontal bar :(v|h) ")
    match share:
        case "v"|'V':
            return '\n'
        case 'H'|'h':
            return''
        case _:
            return None

NEW_LINE = choice()
main()
