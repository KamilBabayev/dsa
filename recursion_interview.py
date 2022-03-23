
# sum of digits of a positive integer number
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'only positive numbers'
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_of_digits(n//10)

# calculate power of number
def power_of_number(base, exp):
    assert exp>=0 and int(exp) == exp, 'the exponent must be positive number'
    if exp == 0:
        return 0
    if exp == 1:
        return base
    else:
        return base * power_of_number(base, exp-1)

def gcd(a, b):
    # print(a, b)
    assert int(a) == a and int(b) == b, 'the numbers must be integer only'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def decimal_to_binary(n):
    if n == 0:
        return 1
    else:
        return n % 2 + 10 * decimal_to_binary(int(n/2))


print("sum of digits: ", sum_of_digits(342))
print("power of numbers: ", power_of_number(2, 4))
print("gcd: ", gcd(48, 18))
print(decimal_to_binary(13))