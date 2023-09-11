def main():
    user_input = input("What time is it? ")
    return meal_time(user_input)


def meal_time(time):
    time = time.replace("a.m.", "").replace("p.m.", "")
    get_hour, get_min = time.split(":")
    get_min_to_hour = float(get_min) / 60
    total_hour = float(get_hour) + get_min_to_hour

    if total_hour >= 7 and total_hour <= 8:
        print("Breakfast time 🍳")
    elif 12 <= total_hour <= 13:
        print("lunch time 🥗🍱")
    elif 18 <= total_hour <= 19:
        print("dinner time 🍝")
    else:
        print("get some water 🙃 and wait")


print(main())
