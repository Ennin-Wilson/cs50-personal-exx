import operator


def main():
    user_input = input("Expression: ")
    return calculator(user_input)


def calculator(expression):
    expression = expression.replace(" ", "")
    first_number, operator_, last_number = expression.split()
    first_number = int(first_number)
    last_number = int(last_number)

    math_operators = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
    }

    for key, value in math_operators.items():
        if key == operator_:
            return value(first_number, last_number)


print(main())
