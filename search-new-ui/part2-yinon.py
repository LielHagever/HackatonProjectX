from consts import *


def input_insert_and_test():
    print("do you want to be a guest or host?")
    answer = input("1) Guest \n2) Host\n3) Exit\n")
    while answer != "1" and answer != "2" and answer != "3":
        print("input must be 1 or 2.  please try again: ")
        answer = input("1) Guest \n2) Host\n")
    if answer == "3":
        print("Thank you for choosing 'DineWithMe'")
        exit()
    return int(answer)


def if_guest_1():
    guest_dict = {}
    num_of_guests = input("how many guests will come? ")
    while not num_of_guests.isnumeric():
        print("please insert a natural number.")
        num_of_guests = input("how many guests will come? ")
    num_of_guests = int(num_of_guests)
    day_of_meal = input("which day?")
    while day_of_meal not in DAY_LIST:
        print("please enter the name of an existing day in lowercase letters. ")
        day_of_meal = input("try again: ")
    type_of_meal = input("what kind of meal do you want?\nb) breakfast\nl) lunch\nd) dinner\n")
    while type_of_meal != "b" and type_of_meal != "l" and type_of_meal != "d":
        print("press on one of the options b or l or d")
        type_of_meal = input("please try again")
    kosher = input("do you prefer kosher food or not?\ny) yes\nn) no\n")
    while kosher != "n" and kosher != "y":
        print("press on one of the options y or n")
        kosher = input("please enter again: ")
    vibe_of_meal = input("what kind of atmosphere you're looking for?\nf) family atmosphere\n"
                         "y) young and energetic atmosphere (18+)\n")
    while vibe_of_meal != "f" and vibe_of_meal != "y":
        print("press on one of the options f or y")
        vibe_of_meal = input("please try again: ")
    status = input("what is your life status?")

    res = f"{num_of_guests}|{day_of_meal}|{type_of_meal}|{kosher}|{vibe_of_meal}|{status}"
    guest_dict["method"] = "search"
    guest_dict["info"] = res
    return guest_dict


def if_host_2():
    host_dict = {}
    num_of_hosts = input("how many people will be? ")
    while not num_of_hosts.isnumeric():
        print("please insert a natural number.")
        num_of_hosts = input("how many people will be? ")
    num_of_hosts = int(num_of_hosts)
    day_of_meal = input("What day would you like to host? (day name)")
    while day_of_meal not in DAY_LIST:
        print("please enter the name of an existing day in lowercase letters. ")
        day_of_meal = input("try again: ")
    type_of_meal = input("what kind of meal do you want to offer?\nb) breakfast\nl) lunch\nd) dinner\n")
    while type_of_meal != "b" and type_of_meal != "l" and type_of_meal != "d":
        print("press on one of the options b or l or d")
        type_of_meal = input("please try again")
    kosher = input("the food will be kosher?\ny) yes\nn) no\n")
    while kosher != "n" and kosher != "y":
        print("press on one of the options y or n")
        kosher = input("please enter again: ")
    vibe_of_meal = input("what kind of atmosphere will be?\nf) family atmosphere\n"
                         "y) young and energetic atmosphere (18+)\n")
    while vibe_of_meal != "f" and vibe_of_meal != "y":
        print("press on one of the options f or y")
        vibe_of_meal = input("please try again: ")

    res = f"{num_of_hosts}|{day_of_meal}|{type_of_meal}|{kosher}|{vibe_of_meal}"
    host_dict["method"] = "new meal"
    host_dict["info"] = res
    return host_dict


user_answer = input_insert_and_test()
if user_answer == 0:
    print(if_guest_1())
else:
    print(if_host_2())
