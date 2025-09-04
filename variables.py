import sys
print("Running with Python interpreter:", sys.executable)
print("")

# Variables are "containers" that store data

# String (text)
name="Gabriel"
surName="Guzman"
vibeIs="Bent out of shape"

# Interger (whole number)
age=47
yearsPast=10

# Float (deciman number)
height=6.1
shrunk=3.2

# Boolean (True/False)
is_learning_python = True
vibe_check=False

# Output the values
print("Name:", name)
print("Age:", age)
print("Heaght:", height)
print("Learning Python:", is_learning_python)
print("Your last name is", surName, ".")
print("In 10 years you will be", age + yearsPast,".")
print("Oh no! A wizard shrunk you. You are now", shrunk,".")
print("Checking your vibe. Your vibe is:", vibeIs,".")
print("Is that true?", vibe_check)
print("")

# Check types

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_learning_python:", type(is_learning_python))
print("")

# Type Conversion Examples

print("\n--- Type Conversion Examples ---")
print("")

# Convert interget to string

age_str = str(age)
print("age_str:", age_str, "| type:", type(age_str))
print("")

# Convert string to interger

year_str = "2025"
year_int = int(year_str)
print("year_int:", year_int, "| type:", type(year_int))
print("")

# Convert string to float

pi_str = "3.14159"
pi_float = float(pi_str)
print("pi_float:", pi_float, "| type:", type(pi_float))
print("")

# Convert boolean into interger

truth = True
truth_as_int = int(truth)
print("truth_as_int:", truth_as_int, "| type:", type(truth_as_int))
print("")

# Convert internet to boolean

zero = 0
nonzero = 42
print("bool(0):", bool(zero))
print("bool(42):", bool(nonzero))
print("")

