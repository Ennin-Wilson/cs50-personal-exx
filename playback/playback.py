def main():
    return pause()


def pause():
    user_input = input("Start your speech recognition process ")
    return user_input.replace(" ", "...")


print(main())
