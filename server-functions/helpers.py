import json
import hashlib


def get_all_users(path='users.json'):
    with open(path, 'r') as users:
        all_users = json.loads(users.read())

    return all_users


def get_user_id_counter(path='user_controller.json'):
    with open(path, 'r') as user_controller:
        id_counter = json.loads(user_controller.read())['id_counter']

    return id_counter


def hash_password(password):
    password_encode = password.encode()
    return hashlib.md5(password_encode).hexdigest()


def check_password(login_password, hashed_password):
    return hashed_password == hash_password(login_password)


def check_username_and_email(username, email):
    users = get_all_users()

    for user in users:
        if user['email'] == email or user['username'] == username:
            return False
    return True


def add_new_user_to_db(user_object, user_path='users.json',
                       user_controller_path='user_controller.json'):
    users = get_all_users()

    if check_username_and_email(user_object['username'], user_object['email']):
        new_password_hash = hash_password(user_object['password'])
        user_object['password'] = new_password_hash

        current_users_id_counter = get_user_id_counter()

        users.append({**user_object, "id": current_users_id_counter + 1})

        with open(user_controller_path, 'w') as user_controller:
            user_controller.write(json.dumps({"id_counter": current_users_id_counter + 1}))

        with open(user_path, 'w') as users_file:
            users_file.write(json.dumps(users))


def find_user(username, password):
    users = get_all_users()

    for user in users:
        if user['username'] == username and check_password(password, user['password']):
            return True, user
    return False, "username or password is incorrect"


def get_user_by_id(user_id):
    users = get_all_users()

    if not len(users):
        return {}

    low = 0
    high = len(users)

    while low < high:
        mid = (low + high) // 2

        if users[mid]['id'] == user_id:
            return users[mid]
        elif users[mid]['id'] > user_id:
            high = mid-1
        elif users[mid]['id'] < user_id:
            low = mid+1

    return {}
