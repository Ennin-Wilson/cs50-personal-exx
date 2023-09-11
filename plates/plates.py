def main():
    user_input = input("Plate: ")
    is_val = valid_plate(user_input)
    if is_val:
        print("Valid")
    else:
        print("Invalid")


def valid_plate(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    not_allowed = [" ", ",", "!", "."]
    for char in plate:
        if char in not_allowed:
            return False

    for x, y in zip(plate, plate[1:]):
        if x.isdigit() and not y.isdigit():
            return False

    for char in plate:
        if char.isdigit():
            if char.startswith("0"):
                return False
            else:
                return True

    return True


main()
