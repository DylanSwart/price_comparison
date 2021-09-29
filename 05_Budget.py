# Component 4 budget

import re

# Functions here


# String Check function
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # If the snack is in the list return full response
        if choice in var_list:

            # Get full name of snack and put it in title case
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # If chosen option is not valid set to no
        else:
            is_valid = "no"

    # If snack is not ok ask question again
    if is_valid == "yes":
        return chosen

    else:
        return "Invalid choice"


# Regular expressions
number_regex = "^[1-9]"

# Lists and dictionaries goes here
valid_food = [
    ["sea salt crackers"],
    ["griffins snax"],
    ["pizza shapes"],
    ["arnotts cheds"],
    ["rosemary wheat"],
    ["original rice crackers"]
]

# Yes No list
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Price dictionary
food_price_dict = {
    'sea salt crackers': 2,
    'griffins snax': 2.5,
    'pizza shapes': 3.3,
    'arnotts cheds': 3.99,
    'rosemary wheat': 2,
    'original rice crackers': 1.65
}

# Initialise variables
food_ok = ""
food = ""
recommendation_1 = "Recommended Order: Original Rice Crackers"
recommendation_2 = "Recommended Order: Sea Salt Crackers/ Rosemary Wheat"
recommendation_3 = "Recommended Order: Griffins Snax"
recommendation_4 = "Recommended Order: Pizza Shapes"
recommendation_5 = "Recommended Order: Arnotts Cheds"

print(valid_food)
print()

food_order = []

# Main routine here

check_food = "Invalid choice"
while check_food == "Invalid choice":
    want_food = input("Do you want food?: ").lower()
    check_food = string_check(want_food, yes_no)

# If user input is yes ask what snacks they want
if check_food == "Yes":

    budget = float(input("What is your budget: $"))

    if budget == 1.65:
        print(recommendation_1)

    elif budget == 2:
        print(recommendation_2)

    elif budget == 2.5:
        print(recommendation_3)

    elif budget == 3.3:
        print(recommendation_4)

    elif budget == 3.99:
        print(recommendation_5)

    desired_food = ""
    while desired_food != "xxx":
        # Ask user for desired snack
        desired_food = input("Order: ").lower()

        for var_list in valid_food:

            # If chosen snack is in valid snacks return full response
            if desired_food in var_list:

                # Get full name of snack and put it in title case
                food = var_list[0].title()
                food_ok = "yes"
                break

            # If chosen snack is not in valid snack set snack ok to no
            else:
                food_ok = "no"

        # If the snack is not ok ask question again
        if food_ok == "yes":
            print("Snack choice: ", food)

        else:
            print("Sorry that was not a option")

            # Exit code
            if desired_food == "xxx":
                break

            if re.match(number_regex, desired_food):
                amount = int(desired_food[0])
                desired_food = desired_food[1:]

            else:
                amount = 1
                desired_food = desired_food

            # Remove white space around desired snack
            desired_food = desired_food.strip()

            # Check if snack is valid
            food_choice = string_check(desired_food, valid_food)

            # Check if snack number is valid
            if amount >= 5:
                print("Sorry we have a max of 4 snacks")
                food_choice = "Invalid choice"

            # Add snack to list
            amount_food = "{} {}".format(amount, food_choice)

            # Check if snack is not exit code
            if food_choice != "xxx" and food_choice != "Invalid choice":
                food_order.append(food_choice)

# Show snack order
print()
if len(food_order) == 0:
    print("Food order: None")

else:
    print("Food Ordered: ")

    for item in food_order:
        print(item)
