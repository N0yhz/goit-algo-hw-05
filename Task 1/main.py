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
