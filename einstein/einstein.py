def main():
    user_input = int(input("Mass: "))
    return convert(user_input)


def convert(mass):
    # E = mc^2
    energy = mass * (300000000**2)
    return f"E: {energy}"


print(main())
