def factorial(n):
    print(n)
    return n * factorial(n - 1)

def factorial2(n):
    assert n >= 1 and int(n) == n, 'number must be positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial2(n-1)

#factorial(3)

print(factorial2(3))