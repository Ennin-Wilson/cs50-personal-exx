def main():
    return snake_case()


def snake_case():
    user_input = input("CamelCase: ")
    user_out = ""
    for char in user_input:
        if char.isupper():
            user_out += f"_{char.lower()}"
        else:
            user_out += char
    return user_out


print(main())
