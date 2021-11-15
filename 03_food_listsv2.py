# Component 2 Food lists Version 2

# Food list
valid_food = [
    ["sea salt crackers"],
    ["griffins snax"],
    ["pizza shapes"],
    ["arnotts cheds"],
    ["rosemary wheat"],
    ["original rice crackers"]
]

# Initialise variables
food_ok = ""
food = ""

print(valid_food)
print()

# Loop program three times
for item in range(0, 3):

    # Ask used for desired food
    desired_food = input("Food: ").lower()

    for var_list in valid_food:

        # If chosen food is in valid food return full response
        if desired_food in var_list:

            # Get full name of food and put it in title case
            food = var_list[0].title()
            food_ok = "yes"
            break

        # If chosen food is not in valid food set food ok to no
        else:
            food_ok = "no"

    # If the food is not ok ask question again
    if food_ok == "yes":
        print("food choice: ", food)

    else:
        print("Sorry that was not a option")
