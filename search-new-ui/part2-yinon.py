def input_insert_and_test():
    answer = input("enter 0 for guest or 1 for host: ")
    while answer != "0" and answer != "1":
        print("input must be 0 or 1!  please try again: ")
        answer = input("enter 0 for guest or 1 for host: ")
    return int(answer)


def host_or_guest():
    print("do you want to be a guest or host?")
    answer = input_insert_and_test()
    if answer == 0:
        status = input("what is ur life situation")
        kosher = input("do you prefer kosher food or not?")


host_or_guest()
