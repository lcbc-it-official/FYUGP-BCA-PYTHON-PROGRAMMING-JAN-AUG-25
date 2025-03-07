# 6. Identity Operators
# These operators are used to compare objects' memory locations.
d = [1, 2, 3]
e = [1, 2, 3]
f = e

'''
print("\nIdentity Operators:")
print("d is e:", d is e)      # Checks if both point to the same object
print("d is not e:", d is not e)  # Checks if they point to different objects
'''

print("e is f:", e is f)      # Checks if both point to the same object
print("e is not f:", e is not f)  # Checks if they point to different objects
