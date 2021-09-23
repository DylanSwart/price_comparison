
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

payment = [
    ["cash", "ca"],
    ["credit", "cr"]
]

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

    how_pay = "Invalid choice"
    while how_pay == "Invalid choice":
        how_pay = input("Please choose a payment option Cash or Credit: ").lower()
        how_pay = string_check(how_pay, payment)

    subtotal = food_price_dict[desired_food]

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal

    else:
        surcharge = 0

    total = subtotal + surcharge
    print(total)
