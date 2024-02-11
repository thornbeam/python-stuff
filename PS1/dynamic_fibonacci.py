import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# start = time.time()
# print(fib(30))
# end = time.time()
# print("with normal fib:", end - start)


def dy_fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            result = dy_fib(n - 2) + dy_fib(n - 1)
            memo[n] = result
            return result

start = time.time()
print(dy_fib(900))
end = time.time()
print("with dynamic fib:", end - start)
