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

