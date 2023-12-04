# Functions

# Creating Functions ------------------------------------------------------------
def greet():
    print("Hello, welcome to functions in Python!")

greet() # Calling Functions


# Function Parameters and Arguments --------------------------------------------
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice") 


# Return Statement ----------------------------------------------------------------
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result) 


# Default Parameters and Keyword Arguments ----------------------------------------
def greet_person(name="Emanuel"):
    print(f"Hello, {name}!")

greet_person()  # Calling the function without an argument
greet_person("Carlos")  # Calling the function with an argument


# Docstrings ----------------------------------------------------------------------
def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: Producto a and b.
    """
    return a * b

print(multiply.__doc__)
print(help(multiply))
print(multiply(5, 6))