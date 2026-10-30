def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number like 5 or 2.5.")
            continue
        if value <= 0:
            print("Must be greater than 0.")
            continue
        return value


if __name__ == "__main__":
    x = get_positive_number("Enter amount: ")
    print(f"Got {x}")