def main():
    amount = input("How much was your meal ")
    tip_percentage = input("What percentage would you like to tip ")
    tip = currencies(amount) * percentage(tip_percentage)
    return f"{tip:.2f}"


def currencies(amount):
    # you can also use dictionary to store all the currencies and loop through them
    return float(amount.replace("$", "").replace("£", "").replace("€", ""))


def percentage(percent):
    return float(percent.replace("%", "")) / 100


print(main())
