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
    return [dish['name'] for dish in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
      chilis = food['heat_level'] * '🌶'
      print(food['name'] + ' (' + food['cuisine'] + ') | Heat Level: ' + chilis)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    found_food = [food for food in spicy_foods if food['cuisine'] == cuisine]
    return found_food[0]


def print_spiciest_foods(spicy_foods):
    for food in get_spiciest_foods(spicy_foods):
        print_spicy_foods([food])


def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat += food['heat_level']
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
