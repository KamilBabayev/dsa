

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'fibonacci number can not be negative or non integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    print(fibonacci(4.5))
except AssertionError:
    print("fibonacci number can not be negative or non integer")
