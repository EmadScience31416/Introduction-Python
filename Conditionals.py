# Conditional statements

# If statement -------------------------------------------
x = 5
if x > 5:
    print('x is greater than 5.')

# If-else statement -------------------------------------
# Example 1:
y = 7
if y % 2 == 0:
    print("y is even.")
else:
    print("y is odd.")

# Example 2:
age = 21
is_usa = True
if (age >= 21 and is_usa == True) or (age >= 18 and is_usa == False):
    print("you're of age.")
else:
    print("you're a minor.")
    
# If-elif-else statement --------------------------------
# Example 1:
z = 20
if z < 0:
    print("z is negative.")
elif z == 0:
    print("z is zero.")
else:
    print("z is positive.")

# Example 2:
level = 3 # Values 1-5
if level == 1:
    print("performance is excellent.")
elif level == 2:
    print("performance is good.")
elif level == 3:
    print("performance is fair.")
elif level == 4:
    print("performance is poor.")
else:
    print("performance is very poor.")

# Example 3 - Nested if statements:
a = 10
b = 20
if a > 5:
    if b > 15:
        print("Both a is greater than 5 and b is greater than 15")
    else:
        print("a is greater than 5 but b is not greater than 15")
else:
    print("a is not greater than 5")

