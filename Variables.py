# Using variables --------------------------------------

greeting = "Hi guys"
print(greeting)

age = 50
print(age)

print(greeting, age)
print("Hello. I'm", age, 'year old.')


# Type of variables ---------------------------------------------

# String (str)
name = 'Juan'
print(type(name))

# Integer (int)
x = 24
print(type(x))

# Float (float)
rate = 0.23
print(type(rate))

# Boolean (bool)
isDoctor = True
print(type(isDoctor))


# Using 'print' ---------------------------------------------------

# Example 1 - concat string

print("Hi guys. I'm Emanuel.")

greeting = "Hi guys" # String
name = 'Emanuel' # String

print(greeting, ". I'm", name, ".") # form 1
print(greeting + ". I'm " + name + ".") # form 2
print(f"{greeting}. I'm {name}.") # form 3


# Example 2 - concat string + number

print("Hello. I'm Emanuel and I wanna tell you that the number pi is equal to 3.1416.")

greeting = 'Hello' # String
name = 'Emanuel' # String
pi = 3.1416 # Float

print(greeting, ". I'm", name, 'and I wanna tell you that the number pi is equal to', pi, '.') # Form 1
print(greeting + " I'm " + name + ' and I wanna tell you that the number pi is equal to ' + str(pi) + '.') # Form 2
print(f"{greeting}. I'm {name} and I wanna tell you that the number pi is equal to {pi}.") # Form 3


# Using 'input' ---------------------------------------------------

name = input("Write your name: ").strip().title()
age = input("Write your age: ").strip()
country = input("¿Where are you?: ").strip()
print(f"Welcome {name}, your age is {age} and your country is {country}.")