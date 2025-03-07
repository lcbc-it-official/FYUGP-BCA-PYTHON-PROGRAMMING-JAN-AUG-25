# 3. Logical Operators
# These operators are used to combine conditional statements.
x = True
y = False
#print("Name: {}, Age: {}, Height: {:.1f}".format(name, age, height))
print("\nUsing Logical Operators on x: {} and y: {}:".format (x, y))
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT

# 4. Bitwise Operators
# These operators perform bit-level operations.
p = 4  # Binary: 100
q = 5  # Binary: 101

print("\nUsing Bitwise Operators on p: {} and q: {}:".format (p, q))
print("p & q =", p & q)  # Bitwise AND
print("p | q =", p | q)  # Bitwise OR
print("p ^ q =", p ^ q)  # Bitwise XOR
print("~p =", ~p)        # Bitwise NOT
print("p << 1 =", p << 1)  # Left Shift
print("p >> 1 =", p >> 1)  # Right Shift
