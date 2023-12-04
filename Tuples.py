# Tuples

# Creating Tuples ---------------------------------------------
tuple1 = (1, 2, 3, 4)
print(tuple1)

tuple2 = ('apple', 'banana', 'cherry')
print(tuple2)

tuple3 = (1, 'hello', True, 3.14)
print(tuple3)


# Accessing Tuple Elements --------------------------------------
print(tuple1[0]) 
print(tuple2[1])  
print(tuple3[-1]) # Negative index -1 refers to the last element


# Tuple Slicing ------------------------------------------------
print(tuple1[1:3])  # Elements at index 1 and 2
print(tuple2[:2])   # Elements up to index 1


# Tuple Immutability -------------------------------------------
tuple4 = (1, 2, 3)
# tuple4[0] = 5


# Tuple Operations --------------------------------------------
tuple5 = tuple1 + tuple2  # Concatenating tuples
print(tuple5)             

tuple6 = tuple3 * 2       # Repeating elements in a tuple
print(tuple6)             

print(len(tuple1))        
print('hello' in tuple3)  





