from bot import add_contact, change_contact, show_phone, get_contacts

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}
    print("Welcome! I am your personal bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Bye!")
            break
        elif command == "hello":
            print("How can I help you today?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(get_contacts(args, contacts))
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
