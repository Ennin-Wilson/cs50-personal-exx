def main():
    return format_text()


def format_text():
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    user_input = input("Input: ")
    user_output = ""
    for char in user_input:
        if char not in vowels:
            user_output += char

    return user_output


print(main())
