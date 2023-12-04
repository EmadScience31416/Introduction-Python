# String

# Creating Strings ------------------------------------------------------------------
message_1 = 'Pyton is good.'
message_2 = "I'm learning python."
message_3 = '''This message is 
multiline string.
'''
message_4 = f'This message is\nother multiline string.'

print(message_1)
print(message_2)
print(message_3)
print(message_4)

# Accessing Characters --------------------------------------------------------------
my_string = "Hi guys"
print(my_string[0]) # Output H
print(my_string[1]) # Output i
print(my_string[-1]) # Output s

print(my_string[0:2]) # Output Hi
print(my_string[3:7]) # Output guys

print(my_string[:2]) # Output Hi
print(my_string[3:]) # Output guys
print(my_string[-4:]) # Output guys

# Basic String Operations ------------------------------------------------------------

# Concatenation
greeting = "Hello"
name = "Emanuel"
message = greeting + ", " + name 
print(message) # Output: 'Hello, Emanuel'

# Repetition
repeated = "abc" * 3
print(repeated) # Output: 'abcabcabc'

# Useful Functions and Methods -------------------------------------------------------

# len()
word = "Pyton"
print(len("Python")) # Output: 6

# upper() and lower()
print(word.upper()) # Output: PYTHON
print(word.lower()) # Output: python

# strip() and title()
word = "      i like python.      "
print(word.strip()) # Output: i like python.
print(word.title()) # Output:       I like python.      
print(word.strip().title()) # Output: I like python.

# split()
sentence = "Python is awesome"
print(sentence.split())  # Output: ['Python', 'is', 'awesome']

# String Formatting -----------------------------------------------------------------

name = "Alice"
age = 30

# format()
sentence = "My name is {} and I'm {} years old.".format(name, age)
print(sentence)

# Using f-strings (Python 3.6+)
sentence = f"My name is {name} and I'm {age} years old."
print(sentence)







