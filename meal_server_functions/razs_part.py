import json
import consts

def get_all_meals():
    with open(consts.MEALS_DB_PATH, 'r') as meals_file:
        all_meals = json.loads(meals_file.read())

    return all_meals

def add_meal(meal_string):
    whole_meal = meal_string.split('|')

    meals = get_all_meals()
    meals.append({"guest number": whole_meal[0], "day in the week": whole_meal[1], "meal kind": whole_meal[2], "kosher": whole_meal[3], "atmosphere": whole_meal[4], "status": whole_meal[5]})

    with open(consts.MEALS_DB_PATH, 'w') as meals_file:
        meals_file.write(json.dumps(meals))


def find_meals(search_ops):
    options = []
    whole_ops = search_ops.split('|')
    gr = {"guest number": whole_ops[0], "day in the week": whole_ops[1], "meal kind": whole_ops[2], "kosher": whole_ops[3], "atmosphere": whole_ops[4], "status": whole_ops[5]}

    meals = get_all_meals()

    for meal in meals:
        for key, value in meal.items():
            for i in whole_ops:
                if value == i:
                    options.append(meal)

    return options

add_meal()

