# Dictionaries

# Creating Dictionaries ---------------------------------------------------------------------------------------------
# Creating an empty dictionary
my_dict = {}
print(my_dict)

# Using dict() constructor with key-value pairs
my_dict = dict(name='Emanuel', favorite_color='blue', weight_kg=90)
print(my_dict)

# Using curly braces {}
my_dict = {'name': 'Emanuel', 'favorite_color': 'blue', 'weight_kg': 90}
print(my_dict)

my_dict = {'name': ['Emanuel', 'Carlos', 'Andrea'], 'favorite_color': ['blue', 'red', 'green'], 'weight_kg': [90, 80, 65]}
print(my_dict)


# Accessing dictionary elements --------------------------------------------------------------------------------------
print(my_dict['name']) 
print(my_dict['weight_kg']) 


# Dictionary Mutability ----------------------------------------------------------------------------------------------

# Modifying dictionaries
my_dict['name'] = ['Juan', 'Javier', 'Pedro']   # Modifying the value for a key
print(my_dict)

my_dict['height'] = [180, 185, 165]   # Adding a new key-value pair
print(my_dict)

del my_dict['weight_kg']    # Deleting a key-value pair
print(my_dict)


# Dictionary Operations ------------------------------------------------------------------------------------------------
print('name' in my_dict)         # Checking if 'apple' key exists

print(my_dict.keys())             # Getting keys
print(my_dict.values())           

print(len(my_dict))               # length of my_dict


# Dictionary methods --------------------------------------------------------------------------------------------------
my_dict.pop('height')             # Removing a key-value pair
print(my_dict)

my_dict.clear()                   # Removing all elements from the dictionary
print(my_dict)                    
