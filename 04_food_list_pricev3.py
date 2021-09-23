# Component 3v2 budget and food list

# Import statements here
import re
import pandas

# Functions here

# String_checker function here
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # If the food is in the list return full response
        if choice in var_list:

            # Get full name of food and put it in title case
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # If chosen option is not valid set to no
        else:
            is_valid = "no"

    # If food is not ok ask question again
    if is_valid == "yes":
        return chosen

    else:
        return "Invalid choice"


# Regular expressions
number_regex = "^[1-9]"

# Variables
food_ok = ""
food = ""
name = "Dylan"

sea_salt_crackers = []
griffins_snax = []
pizza_shapes = []
arnotts_cheds = []
rosemary_wheat = []
original_race_crackers = []

# Lists and dictionaries goes here
valid_food = [sea_salt_crackers, griffins_snax, pizza_shapes, arnotts_cheds, rosemary_wheat, original_race_crackers]

# Yes No list
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Payment Method list
payment = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# Price dictionary
food_price_dict = {
    'sea salt crackers': 2,
    'griffins snax': 2.5,
    'pizza shapes': 3.3,
    'arnotts cheds': 3.99,
    'rosemary wheat': 2,
    'original rice crackers': 1.65,
}

# KG price dictionary
kg_price_dict = {
    'sea salt crackers': 10.81,
    'griffin snax': 10,
    'pizza shapes': 17.37,
    'arnotts cheds': 15.96,
    'rosemary wheat': 11.76,
    'original rice crackers': 16.5
}

movie_data_dict = {
    'Name': name,
    'Sea Salt Crackers': sea_salt_crackers,
    'Griffins Snax': griffins_snax,
    'Pizza Shapes': pizza_shapes,
    'Arnotts Cheds': arnotts_cheds,
    'Rosemary Wheat': rosemary_wheat,
    'Original Rice Crackers': original_race_crackers
}


# Holds food order for one person
food_order = []

# Ask user if they want food
check_food = "Invalid choice"
while check_food == "Invalid choice":
    want_food = input("Do you want food?: ").lower()
    check_food = string_check(want_food, yes_no)

# If user input is yes ask what food they want
if check_food == "Yes":

    desired_food = ""
    while desired_food != "quit":
        # Ask user for desired food
        desired_food = input("food: ").lower()

        food_row = []

        # Exit code
        if desired_food == "quit":
            break

        if re.match(number_regex, desired_food):
            amount = int(desired_food[0])
            desired_food = desired_food[1:]

        else:
            amount = 1
            desired_food = desired_food

        # Remove white space around desired food
        desired_food = desired_food.strip()

        # Check if food is valid
        food_choice = string_check(desired_food, valid_food)

        # Check if food number is valid
        if amount >= 5:
            print("Sorry we have a max of 4 of each food")
            food_choice = "Invalid choice"

        # Add food to list
        amount_food = "{} {}".format(amount, food_choice)

        # Add food and amount to list

        food_row.append(amount)
        food_row.append(food_choice)

        # Check if food is not exit code
        if food_choice != "quit" and food_choice != "Invalid choice":
            food_order.append(food_row)

# Show food order
# Print details

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# Create column called Sub Total
# Fill it with price of tickets and snacks
movie_frame["Sub Total"] = \
    movie_frame['Name'] + \
    movie_frame['Sea Salt Crackers'] * food_price_dict['Sea Salt Crackers'] + \
    movie_frame['Griffin Snax'] * food_price_dict['Griffin Snax'] + \
    movie_frame['Arnotts Cheds'] * food_price_dict['Arnotts Cheds'] + \
    movie_frame['Rosemary Wheat'] * food_price_dict['Rosemary Wheat'] + \
    movie_frame['Original Rice Crackers'] * food_price_dict['Original Rice Crackers']

print(movie_frame)

