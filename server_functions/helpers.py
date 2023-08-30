import json
import hashlib

from server_functions import consts


def get_all_users(path=consts.USERS_DB_PATH):
    with open(path, 'r') as users:
        all_users = json.loads(users.read())

    return all_users


def get_user_id_counter(path=consts.USER_CONTROLLER_PATH):
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


def add_new_user_to_db(user_object, user_path=consts.USERS_DB_PATH,
                       user_controller_path=consts.USER_CONTROLLER_PATH):
    users = get_all_users()

    if check_username_and_email(user_object['username'], user_object['email']):
        new_password_hash = hash_password(user_object['password'])
        user_object['password'] = new_password_hash

        current_users_id_counter = get_user_id_counter()

        users.append(
            {**user_object, "id": current_users_id_counter + 1, "notification": [], "reviews": [], "reviews_to_do": []})

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
        return {}, -1

    low = 0
    high = len(users)-1

    while low <= high:
        mid = (low + high) // 2

        if users[mid]['id'] == user_id:
            return users[mid], mid
        elif users[mid]['id'] > user_id:
            high = mid - 1
        elif users[mid]['id'] < user_id:
            low = mid + 1

    return {}, -1


def get_user_notification(user_id):
    return get_user_by_id(user_id)[0]['notification']


def get_user_reviews(user_id):
    return get_user_by_id(user_id)[0]['reviews']


def add_notification_to_user(user_id, notification_message, user_path=consts.USERS_DB_PATH):
    user, user_index = get_user_by_id(user_id)

    if not user:
        return f'There is no user with id {user_id}'

    users = get_all_users()

    user['notification'].append(notification_message)
    users[user_index] = user

    with open(user_path, 'w') as users_file:
        users_file.write(json.dumps(users))

    return get_user_notification(user_id)


def add_review_to_user(receiver_id, review_dict, user_path=consts.USERS_DB_PATH):
    sender, sender_index = get_user_by_id(review_dict["from"])
    receiver, receiver_index = get_user_by_id(receiver_id)

    if not sender or not receiver:
        if not sender:
            return f'There is no user with {review_dict["from"]}'
        else:
            return f'There is no user with id {receiver_id}'

    users = get_all_users()

    receiver['reviews'].append({"from": review_dict["from"], "message": review_dict["message"]})
    sender['reviews_to_do'].pop(review_dict["review_index"])
    users[receiver_index] = receiver
    users[sender_index] = sender

    with open(user_path, 'w') as users_file:
        users_file.write(json.dumps(users))

    return get_user_reviews(receiver_id)


def add_to_do_review_to_user(user_id, receiver_id, user_path=consts.USERS_DB_PATH):
    user, user_index = get_user_by_id(user_id)

    if not user or not get_user_by_id(receiver_id)[0]:
        if not user:
            return f'There is no user with id {user_id}'
        else:
            return f'There is no user with id {receiver_id}'

    users = get_all_users()

    user['reviews_to_do'].append({"for": receiver_id, "message": ""})
    users[user_index] = user
    print(users)

    with open(user_path, 'w') as users_file:
        users_file.write(json.dumps(users))
