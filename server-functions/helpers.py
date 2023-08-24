import json


def get_all_users():
    with open('users-db/users.json', 'r') as users:
        all_users = json.loads(users.read())

    return all_users


def get_user_id_counter():
    with open('./users-db/user-controller.json', 'r') as user_controller:
        id_counter = json.loads(user_controller.read())['id_counter']

    return id_counter


def check_username_and_email(username, email):
    users = get_all_users()

    for user in users:
        if user['email'] == email or user['username'] == username:
            return False
    return True


def add_new_user_to_db(user_object):
    users = get_all_users()

    if check_username_and_email(user_object['username'], user_object['email']):
        current_users_id_counter = get_user_id_counter()

        users.append({**user_object, "id": current_users_id_counter + 1})

        with open('./users-db/user-controller.json', 'w') as user_controller:
            user_controller.write(json.dumps({"id_counter": current_users_id_counter + 1}))

        with open('./users-db/users.json', 'w') as users_file:
            users_file.write(json.dumps(users))


def find_user(username, password):
    users = get_all_users()

    for user in users:
        if user['username'] == username and user['password'] == password:
            return True, user
    return False, "username or password is incorrect"


def get_user_by_id(user_id):
    users = get_all_users()

    low = 0
    high = len(users)

    while low <= high:
        mid = (low + high) // 2

        if users[mid]['id'] == user_id:
            return users[mid]
        elif users[mid]['id'] > user_id:
            high = mid
        elif users[mid]['id'] < user_id:
            low = mid

    return {}
