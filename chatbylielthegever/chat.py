class Chat:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, message):
        self.messages.append((sender, message))

    def display_messages(self):
        for sender, message in self.messages:
            print(f"{sender}: {message}")


def main():
    chat = Chat()

    user1 = input("Enter name for User 1: ")  # todo put user name poor
    user2 = input("Enter name for User 2: ")  # todo put user name house owner
    # user1 = Fore.RED + user1
    # user2 = Fore.BLUE + user2

    print(f"Welcome, {user1} and {user2}!")

    while True:
        sender = input(f"Who wants to send a message? ({user1}/{user2})(enter 'end' to stop):")
        if sender == user1 or sender == user2:
            message = input("Enter your message: ")
            chat.send_message(sender, message)
        elif sender.lower() == "end":
            print("We hope you enjoyed!")
            print("Your chat:")
            print("---------------------")
            chat.display_messages()
            print("---------------------")
            break
        else:
            print("User incorrect, Try again.")

        chat.display_messages()

        another_message = input("Do you want to send another message? (yes/no):")
        while another_message.lower() == "yes":
            message = input("Enter your message:")
            chat.send_message(sender, message)
            chat.display_messages()
            another_message = input("Do you want to send another message? (yes/no):")
            if another_message.lower() == "yes":
                print("S")  # todo fix code here
            elif another_message.lower() == "no":
                pass


if __name__ == "__main__":
    main()
