# 7. Membership Operators
# These operators check for membership in sequences like strings, lists, or tuples.
a = 10
d = [1,2,3]

print("\nMembership Operators:")
print("2 in d:", 2 in d)  # Checks if 2 is in the list d
print("4 not in d:", 4 not in d)  # Checks if 4 is not in the list d

# 8. Ternary Operator (Conditional Expression)
# This is used to evaluate a condition and return a value.
print("\nTernary Operator:")
result = "Even" if a % 2 == 0 else "Odd"
print(f"The number {a} is {result}.")
