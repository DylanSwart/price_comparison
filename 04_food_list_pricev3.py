# Component 3v2 budget and food list

# Import statements go here

import pandas

all_names = ['Dylan', 'Ryan']

sea_salt_crackers = []
griffins_snax = []
pizza_shapes = []
arnotts_cheds = []
rosemary_wheat = []
original_race_crackers = []

food_list = [sea_salt_crackers, griffins_snax, pizza_shapes, arnotts_cheds, rosemary_wheat, original_race_crackers]

# Data frames dictionary
food_data_dict = {
    'Name': all_names,
    'Sea Salt Crackers': sea_salt_crackers,
    'Griffins Snax': griffins_snax,
    'Pizza Shapes': pizza_shapes,
    'Arnotts Cheds': arnotts_cheds,
    'Rosemary Wheat': rosemary_wheat,
    'Original Rice Crackers': original_race_crackers
}

# cost of each snack
food_price_dict = {
    'Sea Salt Crackers': 2,
    'Griffins Snax': 2.5,
    'Pizza Shapes': 3.3,
    'Arnotts Cheds': 3.99,
    'Rosemary Wheat': 2,
    'Original Rice Crackers': 1.65,
}

test_data = [
    [[2, 'Pizza Shapes'], [1, 'Rosemary Wheat'], [1, 'Griffins Snax'], [2, 'Original Rice Crackers']],
    [[3, 'Pizza Shapes'], [1, 'Sea Salt Crackers'], [1, 'Arnotts Cheds']]
]

count = 0
for client_order in test_data:

    # Assume No snacks have been bought
    for item in food_list:
        item.append(0)

    # Print snack list

    # Get order hard coded for testing
    food_order = test_data[count]
    count += 1

    for item in food_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = food_data_dict[to_find]
            add_list[-1] = amount

print()
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

food_frame.to_csv("food_details.csv")
