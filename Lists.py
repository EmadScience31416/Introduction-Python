# Lists

# Creating a List -----------------------------------------------------
my_list = [] # Creating an empty list
print(my_list)
print(type(my_list))

my_list = [1, 2, 3, 4, 5] # Creating a list with elements
print(my_list)


# Accessing Elements in a List ----------------------------------------
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Accessing the first element
print(my_list[2])  # Accessing the third element


# List Slicing --------------------------------------------------------
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Elements from index 1 to index 3
print(my_list[:3])   # From the beginning to index 2
print(my_list[2:])   # From index 2 to the end


# List Mutability -----------------------------------------------------
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list)  # Replacing the third element with 10

my_list.append(10)  # Adding an element at the end
print(my_list)

my_list.pop(5)  # Removing an element by index
print(my_list)


# List Operations -----------------------------------------------------
list1 = [1, 2, 3]
list2 = ["A", "B", "C"]
list3 = [True, 1, "Hello"]

list4 = list1 + list2  # Concatenating lists
print(list4)           

list5 = list3 * 2      # Repeating elements in a list
print(list5)           

print('Hello' in list3)  # Checking if 'hello' is in list3


# List Methods ---------------------------------------------------------
my_list = [1, 2, 3, 4, 5]

# append()
my_list.append(6)  # Adds 6 at the end
print(my_list)

# insert()
my_list.insert(2, 10)  # Inserts 10 at index 2
print(my_list)

# remove()
my_list.remove(4) # Removes the value 4
print(my_list)

# len()
n = len(my_list) # (Length of the list)
print(n)


# Iterating Through a List --------------------------------------------
# Example 1:
my_list = [10, 20, 30, 40, 50]
for i in my_list:
    print(i)

# Example 2:
colors = ['blue', 'red', 'yellow', 'green', 'grey', 'pink']
favorite_color = 'green'
for color in colors:
    if color == favorite_color:
        print(f'{color.title()} is my favorite color.')
    else:
        print(f"I don't like the color {color}")

# Example 3:
fruits = ['apple', 'banana', 'orange', 'grape', 'watermelon']
for i, fruit in enumerate(fruits):
    print(i)
    print(fruit)

    


