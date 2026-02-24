# Predefined correct username and password
correct_username = "admin"
correct_password = "admin123"

# Read username from standard input
username = input("Enter username: ")

# Read password from standard input
password = input("Enter password: ")

# Check whether both username and password match
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

#output
#Enter username: user
#Enter password: pass123
#Invalid Username or Password
