import helpers


def register(user_string):
    whole_user = user_string.split('|')

    if helpers.check_username_and_email(whole_user[0], whole_user[5]):
        helpers.add_new_user_to_db(
            {"username": whole_user[0], "password": whole_user[1], "age": whole_user[2], "address": whole_user[3],
             "phone": whole_user[4], "email": whole_user[5], "gender": whole_user[6]})
    else:
        print("Username or email is duplicated")
