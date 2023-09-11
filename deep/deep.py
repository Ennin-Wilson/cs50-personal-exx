def main():
    return response()


def response():
    user_response = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    ).lower()
    match user_response:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"


print(main())
