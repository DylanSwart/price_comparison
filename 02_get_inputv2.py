# Component 1 getting user input Version 2

# Not blank function
def not_blank(question, error_message):

    valid = False

    while not valid:
        response = input(question)

        if response != "":

            return response
        else:
            print(error_message)


# Main routine
name = not_blank("Name: ",
                 "Sorry! it appears you left this blank")
