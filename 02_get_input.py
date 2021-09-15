# Component 1 getting user input

# Not blank function
def not_blank(question):

    valid = False

    while not valid:
        response = input(question)

        if response != "":

            return response
        else:
            print("Sorry! it appears you left this blank?")


# Main routine
name = not_blank("Name: ")
