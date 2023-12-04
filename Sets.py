# Sets

# Creating Sets ------------------------------------------------------------------------------
set1 = {1, 2, 3, 4}
print(set1)

set2 = {'apple', 'banana', 'cherry'}
print(set2)

set3 = set([1, 2, 2, 3, 4, 4])  # Using set() function with a list (removes duplicates)
print(set3)


# Set Operations ------------------------------------------------------------------------------
set1.add(5)           # Adding an element to the set
print(set1)           

set2.remove('banana') # Removing an element from the set
print(set2)           

print('apple' in set2)  # Output: True (checking if 'apple' is in set2)


# Set operations (example) --------------------------------------------------------------------
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print(setA.union(setB))         
print(setA.intersection(setB))  
print(setA.difference(setB))


# Set Methods ----------------------------------------------------------------------------------
set3.add(5)          # Adding an element to the set
print(set3)

set3.discard(3)      # Discarding/removing an element
print(set3)

set3.pop()           # Removing and returning an arbitrary element
print(set3)

set3.clear()         # Removing all elements from the set
print(set3)