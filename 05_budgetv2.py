# Component 4 Budget Version 2

# Import Statements
from itertools import combinations

# Functions Go here


def combine(food_price_dict, d):
    return list(combinations(food_price_dict, d))


# Food list
valid_food = [
    ["Sea Salt Crackers"],
    ["Griffins Snax"],
    ["Pizza Shapes"],
    ["Arnotts Cheds"],
    ["Rosemary Wheat"],
    ["Original Rice Crackers"]
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

# Recommendation list
recommendations = [
    ["Original Rice Crackers", 1.65],
    ["Sea Salt Crackers", 2],
    ["Rosemary Wheat", 2],
    ["Griffins Snax", 2.5],
    ["Pizza Shapes", 3.3],
    ["Arnotts Cheds", 3.99]
]

set = 4
print(combine(food_price_dict, set))

