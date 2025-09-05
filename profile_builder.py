# Ask the user for information
name = input("What is your name? ")
age = int(input("How old are you? "))
favorite_food = input("What is your favorite food? ")
# Added Hobby and City for additional variable practice
Hobby = input("What is your favorite hobby? ")
city = input("What city do you live in? ")

# Print a profile summary using f-strings
print("\n--- Profile Summary ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Food: {favorite_food}")
# Adding Hobby and City print statements
print(f"Hobby: {Hobby}")
print(f"City: {city}")

# Adding birth calculation to test age type conversion
birth_year = 2025 - age
print(f"You were born in {birth_year}")