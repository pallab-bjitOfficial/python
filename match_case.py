def run_match(num: int) -> str:

    match num:
        case 1 | 2:
            return "One or two"
        case 3 | 4:
            return "Three or four"
        case 5 | 6:
            return "Five or six"
        case _:
            return "Other"


num = int(input("Enter a number between 1 to 6: "))
print(run_match(num))
