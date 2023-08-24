import json


def test():
    users = [
        {
            "username": "Ayman_Ewida",
            "email": "ayman@gmail.com",
            "password": "Ayman123456@#"
        }
    ]

    with open('./user_test.json', 'w') as users_test:
        users.append({
            "username": "Ayman_Eww",
            "email": "ayman10A@gmail.com",
            "password": "Ayman123456@#"
        })

        users_test.write(json.dumps(users))


test()
