# Component 6 Intro

# Functions go here

# String checker functions
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if food is in one of the lists , return full food
        if choice in var_list:

            # get full food and format
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen

    else:
        print("Please enter a valid option")
        print()
        return "Invalid choice"


# Instructions function
def instructions(options):

    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions?:").lower()
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("Price comparison instructions")
        print()
        print("Please answer all questions.")
        print("If answer is entered wrong it will give you a error message so you know what to fix")
        print("If you want to exit out of an input enter quit")

    return ""

# Main routine


# Yes/ No Dict
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


# Ask if instructions are needed
instructions(yes_no)
print()
print("Program launches")
