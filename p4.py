# List of string numbers
print("Name : Aryan Rana \nRoll No : 1323223")
string_numbers = ["10", "3", "45", "2", "8"]

# Step 1: Convert strings to integers
int_numbers = [int(num) for num in string_numbers]

# Step 2: Sort manually using Bubble Sort
n = len(int_numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if int_numbers[j] > int_numbers[j + 1]:
            # Swap
            int_numbers[j], int_numbers[j + 1] = int_numbers[j + 1], int_numbers[j]

# Step 3: Print sorted list
print("Sorted numbers:", int_numbers)
