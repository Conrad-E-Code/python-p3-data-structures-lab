import ipdb
import statistics
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    return  [f["name"] for f in spicy_foods]

def get_spiciest_foods(spicy_foods):
    pass
    return [f for f in spicy_foods if f["heat_level"] >5]

def print_spicy_foods(spicy_foods):
    pass
    # return [print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level' * '🌶']}  " for food in spicy_foods)]
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}")
# ipdb.set_trace()
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    return [f for f in spicy_foods if f["cuisine"] == cuisine][0]
# ipdb.set_trace()

def print_spiciest_foods(spicy_foods):
    pass
    print_spicy_foods([f for f in spicy_foods if f["heat_level"] > 5])

def get_average_heat_level(spicy_foods):
    pass
    return statistics.mean([f["heat_level"] for f in spicy_foods])

def create_spicy_food(spicy_foods, spicy_food):
    pass
    mylist = list(spicy_foods)
    mylist.append(spicy_food)
    return mylist
# ipdb.set_trace()