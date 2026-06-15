# Personal Information Manager
# My first Python project
# Author: Aishni Rathore

# Build separators using chr() so editors/extensions won't rewrite literal characters
SEP = chr(61) * 40   # '=' repeated 40 times
DASH = chr(45) * 30  # '-' repeated 30 times

# Welcome message
print(SEP)
print("    PERSONAL INFORMATION MANAGER")
print(SEP)
print()

# Store static information
name = "Alex Johnson"   # full name (string)
age = 22                 # age in years (integer)
city = "San Francisco"  # current city (string)
hobby = "playing guitar"# a hobby or interest (string)

# Get user input with basic validation
print("Please tell me about yourself:")
print(DASH)

favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ").strip()

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print(SEP)
print("        YOUR INFORMATION")
print(SEP)
print()
print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food.title()}")
print(f"Favorite Color: {favorite_color.title()}")
print()

# Goodbye message
print(SEP)
print("Thanks for using this program!")
print(SEP)
