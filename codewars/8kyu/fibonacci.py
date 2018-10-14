fibonacci_cache = {}

def fibonacci(n):

    # IF WE HAVE CACHED THE VALUE, THEN RETURN IT

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the nth term
    if n==1:
        value= 1
    elif n == 2:
        value=  1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value

for n in range(1, 1001):
        print (n, ":", fibonacci(n))