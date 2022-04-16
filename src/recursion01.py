
def power_of_two_rec(n):
    if n == 0:
        return 1
    else:
        print(n, 'before')
        power = power_of_two_rec(n - 1)
        print(n, power,  'after')
        return power * 2

def power_of_two_rec2(n):
    if n == 0:
        return 1
    else:
        print(n, 'n before')
        power = power_of_two_rec2(n - 1)
        print(n, 'n after')
        print( 'power', power)
        return power * 2

def power_of_two_iter(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i +1
    return power

def demo(n):
    if n == 0:
        print('below 1')
    else:
        print(n, 'before')
        demo(n-1)
        print(n, 'after')


print(power_of_two_rec2(5))
print(power_of_two_iter(5))
demo(5)
