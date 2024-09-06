def run_match():
    num = int(input("Enter a number between 1 to 6: "))

    match num:
        case 1 | 2:
            print("One or two")
        case 3 | 4:
            print("Three or four")
        case 5 | 6:
            print("Five or six")
        case _:
            print("Other")


run_match()
