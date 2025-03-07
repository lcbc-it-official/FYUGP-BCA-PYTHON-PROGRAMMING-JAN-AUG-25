
def login():
        """Ask an user for their user_name and password
    through the input statement of python
    once the user inputs the data display a greeting msg""" 


        name = input("enter your name: ")
        password = input("enter your password: ")
        print(f"Welcome : {name}")

def get_max(m,n):
    """ Returns the maximm of two numbers"""
    return m>n?m:n

print(get_max(2,3))

def fib(n):  
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    print(f"Displaying Fibonacci numbers LT {n}")
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
n=int (input("Enter a number: "))
fib(n)

