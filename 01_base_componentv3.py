# Base component version 2
# Import statements go here
import pandas
import re

# Functions go here


# Not blank function
def not_blank(question, error_message):

    valid = False

    while not valid:
        response = input(question)

        if response != "":

            return response
        else:
            print(error_message)


# String Checker Function
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


class Solution(object):

    def combinationsum(self, food, target):
        result = []
        unique = {}
        food = list(set(food))
        self.solve(food, target, result, unique)
        return result

    def solve(self, food, target, result, unique, i=0, current=[]):

        if target == 0:
            temp = [i for i in current]
            temp1 = temp
            temp.sort()
            temp = tuple(temp)

            if temp not in unique:
                unique[temp] = 1
                result.append(temp1)
                return

        if target < 0:
            return

        for x in range(i, len(food)):
            current.append(food[x])
            self.solve(food, target-food[x], result, unique, i, current)
            current.pop(len(current)-1)


# Regular Expressions
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
    'Sea Salt Crackers': 2,
    'Griffins Snax': 2.5,
    'Pizza Shapes': 3.3,
    'Arnotts Cheds': 3.99,
    'Rosemary Wheat': 2,
    'Original Rice Crackers': 1.65
}

# Initialise variables
food_ok = ""
food = ""
recommended = ""
all_names = []

sea_salt_crackers = []
griffins_snax = []
pizza_shapes = []
arnotts_cheds = []
rosemary_wheat = []
original_race_crackers = []

food_list = [sea_salt_crackers, griffins_snax, pizza_shapes, arnotts_cheds, rosemary_wheat, original_race_crackers]

print(food_price_dict)
print()

# Food data dictionary
food_data_dict = {
    'Name': all_names,
    'Sea Salt Crackers': sea_salt_crackers,
    'Griffins Snax': griffins_snax,
    'Pizza Shapes': pizza_shapes,
    'Arnotts Cheds': arnotts_cheds,
    'Rosemary Wheat': rosemary_wheat,
    'Original Rice Crackers': original_race_crackers
}

food_order = []

# Main routine
name = not_blank("Name: ",
                 "Sorry! it appears you left this blank")

all_names.append(name)

print()

check_food = "Invalid choice"
while check_food == "Invalid choice":
    want_food = input("Do you want food?: ").lower()
    check_food = string_check(want_food, yes_no)

# If user input is yes ask what foods they want
if check_food == "Yes":

    print()
    budget = float(input("Budget: $"))
    ob1 = Solution()
    recommended = ob1.combinationsum(food_price_dict.values(), budget)
    print(recommended)
    print(food_price_dict)
    print()

    desired_food = ""
    while desired_food != "xxx":
        # Ask user for desired snack
        desired_food = input("snack: ").lower()

        # Exit code
        if desired_food == "xxx":
            break

        # Remove white space around desired snack
        desired_food = desired_food.strip()

        # Check if snack is valid
        food_choice = string_check(desired_food, valid_food)

        if re.match(number_regex, desired_food):
            amount = int(desired_food[0])
            desired_food = desired_food[1:]

        else:
            amount = 1
            desired_food = desired_food

        # Check if snack number is valid
        if amount >= 5:
            print("Sorry we have a max of 4 snacks")
            food_choice = "Invalid choice"

        # Add snack to list
        amount_food = "{} {}".format(amount, food_choice)

        # Check if snack is not exit code
        if food_choice != "xxx" and food_choice != "Invalid choice":
            food_order.append(food_choice)

    for item in food_list:
        item.append(0)

    for item in food_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = food_data_dict[to_find]
            add_list[-1] = amount

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

food_frame = food_frame.rename(columns={'Sea Salt Crackers': 'SSC',
                                        "Original Rice Crackers": 'ORC'})

# Prints food frame out
print(food_frame)

# Puts food frame into a csv file so it can be read
food_frame.to_csv("food_details.csv")
