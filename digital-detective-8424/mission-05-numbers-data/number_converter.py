def main():
    raw_value = input("Enter a positive decimal integer: ").strip()
    number = int(raw_value)

    if number < 0:
        print("Please enter a positive decimal integer.")
        return

    binary_result = bin(number)
    hex_result = hex(number)

    print(f"Decimal: {number}")
    print(f"Binary: {binary_result}")
    print(f"Hexadecimal: {hex_result}")


if __name__ == "__main__":
    main()
