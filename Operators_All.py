# Python program to demonstrate the usage of all operators

# 1. Arithmetic Operators
# These operators are used to perform basic mathematical operations.
a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus (remainder)
print("a // b =", a // b)  # Floor division
print("a ** b =", a ** b)  # Exponentiation

# 2. Relational (Comparison) Operators
# These operators compare two values and return a boolean result.
print("\nRelational Operators:")
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# 3. Logical Operators
# These operators are used to combine conditional statements.
x = True
y = False

print("\nLogical Operators:")
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT

# 4. Bitwise Operators
# These operators perform bit-level operations.
p = 4  # Binary: 100
q = 5  # Binary: 101

print("\nBitwise Operators:")
print("p & q =", p & q)  # Bitwise AND
print("p | q =", p | q)  # Bitwise OR
print("p ^ q =", p ^ q)  # Bitwise XOR
print("~p =", ~p)        # Bitwise NOT
print("p << 1 =", p << 1)  # Left Shift
print("p >> 1 =", p >> 1)  # Right Shift

# 5. Assignment Operators
# These operators assign values to variables and can combine assignment with arithmetic.
c = 7

print("\nAssignment Operators:")
c += 3  # Equivalent to c = c + 3
print("c += 3:", c)
c -= 2  # Equivalent to c = c - 2
print("c -= 2:", c)
c *= 2  # Equivalent to c = c * 2
print("c *= 2:", c)
c /= 3  # Equivalent to c = c / 3
print("c /= 3:", c)
c %= 2  # Equivalent to c = c % 2
print("c %= 2:", c)

# 6. Identity Operators
# These operators are used to compare objects' memory locations.
d = [1, 2, 3]
e = [1, 2, 3]

print("\nIdentity Operators:")
print("d is e:", d is e)      # Checks if both point to the same object
print("d is not e:", d is not e)  # Checks if they point to different objects

# 7. Membership Operators
# These operators check for membership in sequences like strings, lists, or tuples.
print("\nMembership Operators:")
print("2 in d:", 2 in d)  # Checks if 2 is in the list d
print("4 not in d:", 4 not in d)  # Checks if 4 is not in the list d

# 8. Ternary Operator (Conditional Expression)
# This is used to evaluate a condition and return a value.
print("\nTernary Operator:")
result = "Even" if a % 2 == 0 else "Odd"
print(f"The number {a} is {result}.")

# 9. Special Operator: `is` for object identity
# Demonstrated above in Identity Operators.
