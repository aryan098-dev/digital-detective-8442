def decimal_to_binary(number):
    return bin(number)


def decimal_to_hexadecimal(number):
    return hex(number)


def main():
    try:
        number = int(input("Enter a decimal number: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    print("Binary:", decimal_to_binary(number))
    print("Hexadecimal:", decimal_to_hexadecimal(number))


if __name__ == "__main__":
    main()
