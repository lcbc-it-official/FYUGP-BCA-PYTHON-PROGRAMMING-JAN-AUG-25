def main():
    """
    Main function to demonstrate different output formatting options in Python.
    """
    # Using f-strings (Python 3.6+)
    name = "Alice"
    age = 30
    height = 5.7

    print("Using f-strings:")
    print(f"Name: {name}, Age: {age}, Height: {height:.1f}")
    print()

    # Using the format() method
    print("Using the format() method:")
    print("Name: {}, Age: {}, Height: {:.1f}".format(name, age, height))
    print()

    # Using the % operator
    print("Using the % operator:")
    print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))
    print()

    # Formatting numbers with commas as thousands separators
    number = 1234567890
    print("Formatting numbers with commas as thousands separators:")
    print(f"Number: {number:,}")
    print()

    # Formatting numbers with leading zeros
    print("Formatting numbers with leading zeros:")
    print(f"Number: {number:010}")
    print()

    # Formatting numbers as percentages
    percentage = 0.85
    print("Formatting numbers as percentages:")
    print(f"Percentage: {percentage:.2%}")
    print()

    # Aligning text
    print("Aligning text:")
    print(f"{'Left aligned':<15} | {'Center aligned':^15} | {'Right aligned':>15}")
    print()

# Entry point of the script
if __name__ == "__main__":
    main()
