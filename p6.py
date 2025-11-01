# Two sample lists
print("Name : Aryan Rana \nRoll No : 1323223")
list1 = [1, 2, 3, 4, 5, 5, 2]
list2 = [4, 5, 6, 7, 5, 4]

# Using sets to find unique common elements
common_elements = list(set(list1) & set(list2))

# Print result
print("Unique common elements:", common_elements)
