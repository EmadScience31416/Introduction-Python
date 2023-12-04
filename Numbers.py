# Numbers 

# Arithmetic Operators ------------------------------------------------------------
x = 10
y = 3

z = x + y
print(f"Sum between {x} and {y} is {z}")

z = x - y
print(f"Diff between {x} and {y} is {z}")

z = x * y
print(f"Multiplication between {x} and {y} is {z}")

z = x / y
print(f"Division between {x} and {y} is {z}")

z = x // y
print(f"Quotient between {x} and {y} is {z}")

z = x % y
print(f"Remainder between {x} and {y} is {z}")

z = x ** y
print(f"Exponetiation between {x} and {y} is {z}")

# Compound Assignment Operators ------------------------------------------------------------
a = 10
a = a + 1 
print(a)

a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)

# Comparison Operators ------------------------------------------------------------------
x = 5
y = 7

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)  # Output: False
print(x < y)  # Output: True

# Logical Operators
print(6 > 1 and 8 < 5)  # Output: False
print(6 > 1 or 8 < 5)   # Output: True

print(True and False)  # Output: False
print(True or False)   # Output: True

print(not(20 != 10))  # Output: False
print(not(20 < 10))  # Output: True

print((6 > 5 or 9 < 2) and (not(5 > 8) and 6 == 6)) # Output: True