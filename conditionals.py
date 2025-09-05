# Practicing basic Conditionals (if, elif, and else)

#age = int(input("What is your age? " ))

#if age >= 18:
#    print("You are an adult. \n")
#else:
#    print("You are a minor. \n")

# Multiple elif statements practice

#score = int(input("Enter your test score: "))

#if score >= 90:
#    print("Grade: A \n")
#elif score >= 80:
#    print("Grade: B \n")
#elif score >= 70:
#    print("Grade: C \n")
#elif score >= 60:
#    print("Grade: D \n")
#else:
#    print("Grade: F \n")


# Practicint AND, OR statements

#age = int(input("What is your age? "))
#has_id = True

#if age >= 18 and has_id:
#    print("You may enter the club. \n")
#else:
#    print("Access denied! \n")

# Everything above was commented out for this next task. 

#age = int(input("What is your age? "))

#if age < 18:
#   print("Sorry, you cannot vote.")
#   exit()
#else:
#   print("Below enter 1 for Yes, or 2 for No.")

#voter_registration = int(input("Are you registered to vote? "))

#if age >= 18 and voter_registration == 1:
#   print("You can vote!")
#elif age < 18:
#   print("Sorry, you cannot vote.")
#   exit()
#else:
#   print("Sorry, you cannot vote.")

# Sage's cleaner version of my code above commented out

age = int(input("What is your age? "))

if age < 18:
    print("Sorry, you cannot vote.")
else:
    print("Below enter 1 for Yes, or 2 for No.")
    voter_registration = int(input("Are you registered to vote? "))

    if voter_registration == 1:
        print("You can vote!")
    else:
        print("Sorry, you cannot vote.")