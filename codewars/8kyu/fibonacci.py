# from functools import lru_cache
# # least recently used cache
#
#
# @lru_cache(maxsize=1000)
# def fibonacci(n):
#
#     # IF WE HAVE CACHED THE VALUE, THEN RETURN IT
#
#     # Compute the nth term
#     if n==1:
#         return 1
#     elif n == 2:
#         return  1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# for n in range(1, 5000):
#         print (n, ":", fibonacci(n))


def fib  (n):
    if n ==1 or n ==2:
        return 1
    return fib (n-1) + fib (n-2)

print (fib (20))