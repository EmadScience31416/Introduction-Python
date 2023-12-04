# Loops

# 'for' Loops -------------------------------
# Example 1:
for i in range(1,6):
    print(i)

# Example 2:
for _ in range(5):
    print('ring')

# 'while' Loops -------------------------------
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment the count by 1 in each iteration

# Loop Control Statements --------------------
# Using break and continue in a loop
for i in range(1, 6):
    if i == 3:
        continue  # Skip printing number 3
    if i == 5:
        break  # Stop the loop when i is 5
    print(i)
else: 
    print("Loop finished without encountering break")
