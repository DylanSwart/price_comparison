# Component 3v2 budget and food list

# Functions go here


# Lists and dictionaries goes here

valid_food = [
    ["sea salt crackers"],
    ["griffins snax"],
    ["pizza shapes"],
    ["arnotts cheds"],
    ["rosemary wheat"],
    ["original rice crackers"]
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

kg_price = {
    'sea salt crackers': 10.81,
    'griffin snax': 10,
    'pizza shapes': 17.37,
    'arnotts cheds': 15.96,
    'rosemary wheat': 11.76,
    'original rice crackers': 16.5
}

# Initialise variables
food_ok = ""
food = ""

print(valid_food)
print()

# Loop program three times
for item in range(0, 3):

    # Ask used for desired snack
    desired_food = input("Food: ").lower()

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


