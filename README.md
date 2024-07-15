# goit-algo-hw-05
ДЗ Модуль 5

**1. Cache**

```
def catching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
         
         #counting "n" in fibonacci
        if n <= 0:                                             
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fibonacci(n-1) + fibonacci (n-2)
        
         #saving in cache
        cache[n] = result
        return result
    
    return fibonacci

fib = catching_fibonacci()

print(fib(10))
print(fib(15))
```
**2. Find real numbers**

```
import re
from typing import Callable

#Find real numbers

def generator_numbers(text: str):
    pattern = re.compile(r'\b\d+\.\d+\b')
    matches = pattern.findall(text)
    for match in matches:
        yield float(match)
     
def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів.'

# Calling a function to calculate the total income

total_income = sum_profit(text, generator_numbers)
print(f'Total income: {total_income}')
```


**4. Def input_error**

*Main.py*
```
from parse import parse_input
from actions import handle_command

if __name__ == '__main__':            
        print('welcome to the assistant bot!')
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        result = handle_command(command,args)
        print(result)
```

*Parse.py*

```
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
```

*Actions.py*

```
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
            return'Enter [username]'
        except Exception:
            return 'Something went wrong.'
    return inner

@input_error
def add_contacts(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added'

@input_error
def change_contacts(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f'Contact {name} phone has been updated to {new_phone}.'
    else:
        return 'Contact not found'

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f'{name} phone number is {contacts[name]}.'
    else:
        return 'Contact not found.'

@input_error    
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
```

