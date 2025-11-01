print("Name : Aryan Rana \nRoll No : 1323223")
# Predefined username and password
USERNAME = "admin"
PASSWORD = "12345"

# Ask user for input
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

# Check credentials
if entered_username.lower() == USERNAME and entered_password.lower() == PASSWORD:
    print("Login successful! Welcome,", entered_username)
else:
    print("Invalid username or password. Please try again.")
