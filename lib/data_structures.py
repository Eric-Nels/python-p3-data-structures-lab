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
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
        else:
            None
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    for food in spiciest_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level}')            

def get_average_heat_level(spicy_foods):
    heat_levels = []
    for food in spicy_foods:
        heat_levels.append(food["heat_level"])
    if len(heat_levels) == 0:
        return 0
    else: 
        total = sum(heat_levels)
        average = total/len(heat_levels)
        return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
