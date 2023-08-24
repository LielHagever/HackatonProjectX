import helpers


def login(username_password_str):
    username = username_password_str.split('|')[0]
    password = username_password_str.split('|')[1]

    find_user_result, result_message = helpers.find_user(username, password)

    if find_user_result:
        return result_message

    else:
        print(result_message)
