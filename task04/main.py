from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print(func.__name__)
            if func.__name__ in ('add_contact', 'change_contact'):
                return "Enter the name and phone please."
            elif func.__name__ == 'show_phone':
                return "Enter the phone please."
            else:
                return "Enter the argument for the command."
        except KeyError:
            return "Contact not exist."
        except IndexError:
            return "Contact list is empty."
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    
    name, phone = args
    if name in contacts:
        change_input = input(f"Do you want to change phone for {name}? y/n: ")
        if change_input == 'y':
            return change_contact(args, contacts)
        else:
            return "Contact not updated."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        add_input = input("Contact not exist. Do you want to add this contact? y/n: ")
        if add_input == 'y':
            return add_contact(args, contacts)
        else:
            return "New contact not added."

@input_error        
def show_phone(args, contacts):
    if not args:
        raise ValueError

    name, = args
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error  
def show_all(contacts):
    if not contacts:
        raise IndexError

    all_contacts = ''
    for name, phone in contacts.items():
        all_contacts += f'{name}: {phone}\n'
    return all_contacts.strip()

def show_help():
    help_info = '''
        hello - just text greetings
        add - add [name] [phone]: adding new contact with phone
        change - change [name] [phone]: change existing contact phone
        phone - phone [name]: show phone of contact
        all - show all contacts with phones
        close - close the program
        exit - close the program
        help - show all existing commands
    '''
    return help_info

def parse_input(user_input):
    user_input = user_input.strip()
    if not user_input:
        return "", []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Print 'help' for list of existing commands")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == 'help':
            print(show_help())
        elif not command:
            print('Command is empty. Print "help" for list of existing commands.')
        else:
            print('Invalid command. Print "help" for list of existing commands.')

if __name__ == "__main__":
    main()