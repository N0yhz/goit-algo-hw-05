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