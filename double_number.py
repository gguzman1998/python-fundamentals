# Ask the user for a number
#user_input = input("Enter a number: ")

# TODO: Convert user_input to an integer (or float) and double it

# TODO: Print the doubled result

# Convert to integer

#user_input_int = int(user_input)
#user_input_int = user_input_int * 2
#print("Doubled integer: ", user_input_int)

# Convert existing integer to float

#user_input_float = float(user_input_int)
#user_input_float = user_input_float + .23
#user_input_float = user_input_float * 2
#print("Doubled float:", user_input_float)

# Lines 1-19 were commented out for the next skills test. 

user_input = input("Enter a number: ")

try:
    # TODO: Convert to float and double
    number = float(user_input)
    result = number * 2
    print("Double is:", result)

except ValueError:
    # TODO: Print a friendly error message
    print("That’s not a valid number! Please try again.")
