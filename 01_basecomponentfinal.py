# Base component version 2
# Import statements go here

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


# Instructions function
def instructions(options):

    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions?: ").lower()
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print("----------------------------------")
        print("$$$ Price comparison instructions $$$")
        print("----------------------------------")
        print("Please answer all questions.")
        print()
        print("If answer is entered wrong it will give you a error message so you know what to fix")
        print()
        print("If you want to exit out of an input enter quit")
        print("----------------------------------")

    return ""


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
recommended = ""

print(food_price_dict)
print("----------------------------------")

food_order = []
instructions(yes_no)

# Main routine
name = not_blank("Name: ",
                 "Sorry! it appears you left this blank")
print("----------------------------------")

check_food = "Invalid choice"
while check_food == "Invalid choice":
    want_food = input("Do you want food?: ").lower()
    check_food = string_check(want_food, yes_no)

# If user input is yes ask what snacks they want
if check_food == "Yes":

    print("----------------------------------")
    budget = float(input("Budget: $"))
    ob1 = Solution()
    recommended = ob1.combinationsum(food_price_dict.values(), budget)
    print(recommended)
    print(food_price_dict)
    print("----------------------------------")

    desired_food = ""
    while desired_food != "quit":
        # Ask user for desired snack
        desired_food = input("snack: ").lower()

        # Exit code
        if desired_food == "quit":
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
        if food_choice != "quit" and food_choice != "Invalid choice":
            food_order.append(food_choice)

# Show snack order
print()
if len(food_order) == 0:
    print("Food order: None")

else:
    print("Food Ordered: ")

    for item in food_order:
        print(item)
