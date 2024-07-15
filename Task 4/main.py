from parse import parse_input
from actions import handle_command

if __name__ == '__main__':            
        print('welcome to the assistant bot!')
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        result = handle_command(command,args)
        print(result)