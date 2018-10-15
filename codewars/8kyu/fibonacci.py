from functools import lru_cache
# least recently used cache


@lru_cache(maxsize=1000)
def fibonacci(n):

    # IF WE HAVE CACHED THE VALUE, THEN RETURN IT

    # Compute the nth term
    if n==1:
        return 1
    elif n == 2:
        return  1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(1, 11):
        print (n, ":", fibonacci(n))