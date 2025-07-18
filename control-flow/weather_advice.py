# weather_advice.py

# Objective: Provide clothing recommendations based on user-inputted weather conditions.

# 1. Prompt User for Weather Input
# Ask the user to input the current weather from a predefined set of conditions.
# Use .lower() and .strip() to make the input case-insensitive and remove extra spaces.
weather_input = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip()

# 2. Provide Clothing Recommendations using if, elif, and else statements
# Check the user's input against the predefined conditions.
if weather_input == "sunny":
    # If the weather is "sunny", recommend specific clothing.
    print("Wear a t-shirt and sunglasses.")
elif weather_input == "rainy":
    # If the weather is "rainy", recommend specific clothing.
    print("Don't forget your umbrella and a raincoat.")
elif weather_input == "cold":
    # If the weather is "cold", recommend specific clothing.
    print("Make sure to wear a warm coat and a scarf.")
else:
    # Handle unexpected input by printing a generic message.
    print("Sorry, I don't have recommendations for this weather.")

# The program will automatically output the recommendation after the conditional checks.
