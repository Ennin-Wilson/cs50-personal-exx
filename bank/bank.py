def main():
    return deal()


def deal():
    user_input = input("Greeting: ")
    if user_input.startswith("hello"):
        return "0"
    elif user_input.startswith("h"):
        return "$20.00"
    else:
        return "$100.00"


print(main())
