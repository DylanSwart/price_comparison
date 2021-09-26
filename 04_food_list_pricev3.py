# Component 3v2 budget and food list

# Import statements go here
import re
import pandas

# Functions go here


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

# Food list for data frame
food_list = [sea_salt_crackers, griffins_snax, pizza_shapes, arnotts_cheds, rosemary_wheat, original_race_crackers]

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

# Valid food list
valid_food = [
    ["Sea Salt Crackers"],
    ["Griffins Snax"],
    ["Pizza Shapes"],
    ["Arnotts Cheds"],
    ["Rosemary Wheat"],
    ["Original Rice Crackers"]
]

# Price dictionary
food_price_dict = {
    'Sea Salt Crackers': 2,
    'Griffins Snax': 2.5,
    'Pizza Shapes': 3.3,
    'Arnotts Cheds': 3.99,
    'Rosemary Wheat': 2,
    'Original Rice Crackers': 1.65,
}

# KG price dictionary
kg_price_dict = {
    'Sea Salt Crackers': 10.81,
    'Griffin Snax': 10,
    'Pizza Shapes': 17.37,
    'Arnotts Cheds': 15.96,
    'Rosemary Wheat': 11.76,
    'Original Rice crackers': 16.5
}

# Food data dictionary for dataframes
food_data_dict = {
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

# Main Routine here

print(food_price_dict)
print()

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

food_frame = pandas.DataFrame(food_data_dict)
food_frame = food_frame.set_index('Name')

# Create column called Sub Total
# Fill it with price of tickets and snacks
food_frame["Sub Total"] = \
    food_frame['Sea Salt Crackers'] * food_price_dict['Sea Salt Crackers'] + \
    food_frame['Griffins Snax'] * food_price_dict['Griffins Snax'] + \
    food_frame['Pizza Shapes'] * food_price_dict['Pizza Shapes'] + \
    food_frame['Arnotts Cheds'] * food_price_dict['Arnotts Cheds'] + \
    food_frame['Rosemary Wheat'] * food_price_dict['Rosemary Wheat'] + \
    food_frame['Original Rice Crackers'] * food_price_dict['Original Rice Crackers']

print(food_frame)
