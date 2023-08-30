def get_info():  # getting the information
    print("Welcome to DineWithMe!")
    print("------------------------")
    print("Choose an action to perform")
    print("-For Login enter 1")
    print("-For Register enter 2")
    print("-To exit enter 3")
    user_choice = int(input())
    if user_choice < 1 or user_choice > 3:
        return -1
    else:
        return user_choice


# -------------------------------------------------

def at_login():  # in case of login
    username = input("please enter your username:")
    password = input("please enter your password:")
    login_result = username + '|' + password
    return login_result


# ------------------------------------------------------
def at_register():  # in case of register
    username = input("please create username:")
    password = input("please create password:")
    password_again = input("please enter password again:")

    while password != password_again:
        print('Passwords does not match')
        password_again = input("please enter password again:")
    while len(password) < 8 or len(password) < 8:
        print('Password must contain least 8 letters')
        password = input("please enter password again:")
        password_again = input("please enter password again:")

    age = input("please enter age")
    while not age.isnumeric():
        print("age cannot be a word")
        age = input("please enter age again: ")
    while int(age) < 18 or int(age) > 120:
        print("age cannot be under 18 or above 120")
        age = int(input("please enter age"))

    adress = input("enter your adress")
    telephone = input("enter your phone number")
    while len(telephone) < 10 or len(telephone) > 10 or not telephone.isnumeric():
        print("Phone number digits must include 10 numbers only")
        telephone = input("enter your phone number")

    email = input("please enter e-mail")
    while '@' not in email or '.' not in email:
        print("enter valid email")
        email = input("please enter e-mail")
    while email[:email.find('@')] == "" or email[email.find('@') + 1:email.find('.')] == "" or email[email.find(
            '.') + 1:] == "":
        print("enter valid email")
        email = input("please enter e-mail")

    gender = input("please enter your gender")

    register_result = username + "|" + password + "|" + age + "|" + adress + "|" + telephone + "|" + email + "|" + gender

    return register_result


# --------------------------------------------------------------------------------------------------------------------------
def main_ui():  # main - connects al the functions
    result = get_info()
    while result == -1:
        print("Error-number cannot be larger than 3 or smaller than 1")
        result = get_info()

    if result == 1:
        return {
            "output": at_login(),
            "method": "login"
        }
    elif result == 2:
        return {
            "output": at_register(),
            "method": "register"
        }
    elif result == 3:
        print("Have a good day!")
        exit()


# -----------------------------------------------------------------------------
print(main_ui())
