from parse import parse_input

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter [username]'
        except ValueError:
            return 'Give me [name] and [phone] please.'
        except IndexError:
            return 'Enter [username]'
        except Exception as e:
            return str(e)
    return inner

def add_contacts(args, contacts):
    if len(args) != 2:
        return 'Invalid arguments. Usage: add [name] [new phone]'
    name, phone = args
    contacts[name] = phone
    return 'Contact added'

def change_contacts(args, contacts):
    if len(args) != 2:
        return 'Invalid arguments. Usage: change [name] [new phone]'
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f'Contact {name} phone has been updated to {new_phone}.'
    else:
        return 'Contact not found'

def show_phone(args, contacts):
    if len(args) != 1:
        return 'Invalid arguments. Use: phone [name]'
    name = args[0]
    if name in contacts:
        return f'{name} phone number is {contacts[name]}.'
    else:
        return 'Contact not found.'
    
def handle_command(command,args):
    contacts = {}

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in {'close', 'exit'}:
            print('Bye')
            break
        elif command == 'hello':
            print('How can I help you ?')

        elif command == 'add':
            print(add_contacts(args,contacts))
        
        elif command == 'change':
            print (change_contacts(args,contacts))
        
        elif command == 'phone':
            print(show_phone(args, contacts) )
        else:
            return 'Unknown command.'