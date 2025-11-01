# Sample list
print("Name : Aryan Rana \nRoll No : 1323223")
my_list = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Dictionary to store frequency
frequency = {}

# Count frequency
for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Print the result
print("Frequency of elements:")
for key, value in frequency.items():
    print(f"{key}: {value}")