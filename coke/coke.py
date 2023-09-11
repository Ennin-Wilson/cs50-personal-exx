def main():
    return coke_machine()


def coke_machine():
    while True:
        amount_due = 50
        change_owed = 0
        print(f"Amount Due: {amount_due}")
        inset_coin = int(input("Insert Coin: "))

        if 5 != inset_coin != 10 and 25 != inset_coin:
            return f"Amount Due: {amount_due}"

        if inset_coin < amount_due:
            amount_due -= inset_coin

            while True:
                print(f"Amount_due: {amount_due}")
                inset_coin = int(input("Insert Coin:"))

                if 5 != inset_coin != 10 and 25 != inset_coin:
                    return "Amount Due 50"

                if inset_coin < amount_due:
                    amount_due -= inset_coin
                    continue

                else:
                    change_owed += inset_coin - amount_due
                break

        return f"Change Owed: {change_owed}"


print(main())
