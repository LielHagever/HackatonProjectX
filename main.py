from server_ui import LielsPhase1
from server_functions import login, register
from search_new_ui import part2_yinon
from meal_server_functions import razs_part

import json


def main():
    with open("current_user.json", 'r') as current_user_file:
        current_user = json.loads(current_user_file.read())

    if len(current_user) == 0:
        choose_method = LielsPhase1.main_ui()

        if choose_method["method"] == "register":
            current_user = register.register(choose_method["output"])
        elif choose_method["method"] == "login":
            current_user = login.login(choose_method["output"])

        if type(current_user) == str:
            print(current_user)
        else:
            with open("current_user.json", 'w') as current_user_file:
                current_user_file.write(json.dumps(current_user))

    else:
        is_running = True

        while is_running:
            meal_choose_method = part2_yinon.main_ui(current_user)

            if meal_choose_method["method"] == "new_meal":
                razs_part.add_meal(meal_choose_method["info"])
                print("New meal added!")
            elif meal_choose_method["method"] == "search":
                found_meals = razs_part.find_meals(meal_choose_method["info"])
                print(found_meals)


if __name__ == '__main__':
    main()
