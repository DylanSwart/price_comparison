
import re
import pandas


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

food_list = [sea_salt_crackers, griffins_snax, pizza_shapes, arnotts_cheds, rosemary_wheat, original_race_crackers]

valid_food = [
    ["sea salt crackers"],
    ["griffins snax"],
    ["pizza shapes"],
    ["arnotts cheds"],
    ["rosemary wheat"],
    ["original rice crackers"]
]


food_price_dict = {
    'sea salt crackers': 2,
    'griffins snax': 2.5,
    'pizza shapes': 3.3,
    'arnotts cheds': 3.99,
    'rosemary wheat': 2,
    'original rice crackers': 1.65
}

food_data_dict = {
    'Name': name,
    'Sea Salt Crackers': sea_salt_crackers,
    'Griffins Snax': griffins_snax,
    'Pizza Shapes': pizza_shapes,
    'Arnotts Cheds': arnotts_cheds,
    'Rosemary Wheat': rosemary_wheat,
    'Original Rice Crackers': original_race_crackers
}

payment = [
    ["cash", "ca"],
    ["credit", "cr"]
]

food_order = []

print(valid_food)
print()

# Loop program three times
for item in range(0, 3):

    # If user input is yes ask what food they want

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
