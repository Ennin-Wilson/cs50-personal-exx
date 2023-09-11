def main():
    return face_converter()


def face_converter():
    user_input = input("Please enter ")
    swap = {
        ":)": "😄",
        ":(": "🙁",
    }
    for key, value in swap.items():
        user_input = user_input.replace(key, value)
    return user_input


print(main())
