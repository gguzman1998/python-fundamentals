# Collecting user inputs (Name, Age, and Height)

name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)
height = input("How tall are you? ")
height = float(height)
print(f"Your name is {name}, you are {age} years old, and you are {height} inches tall.")
print("")

# Asking user for full name, then using f-strings to print the name

fName = input("Please enter your first name. ")
lName = input("Please enter your last name. ")
print(f"Hello {fName} {lName}. It's a pleasure to meet you. ")
print("")

# Using Conditionals to verify if number is pos, net, or zero

print("Next, you will enter a number. ")
print("The number can be a positive number, a negative number, or zero")
number = input("Please enter a number. ")
number = int(number)
if number > 0:
    print(f"You've entered a positive number. {number}")
elif number < 0:
    print(f"You've entered a negative number. {number}")
else:
    print(f"You've entered zero. {number}")

   