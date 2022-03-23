## Data Structures and Algoritms

Types of Data Structures(DS from now on). DS can be broadly grouped into 2 basic types:
1. `Primitive` 
   - Integer
   - Float
   - Characher
   - String
   - Boolean
2. `None Primitive (User Defined DS)`
Non Primites DS are combining 2 or more primitive ds. Non primitive ds can
be subdivied as: Linear and Non Linear DS.
- `Linear`  - data items are arranged in memory in linear sequential manner, they can be either `static` or `dynamic`.
  - `static` - associated memory locations are fixed at compile time. 
               ex: `array`
  - `dynamic` - associated memory locations change.
                ex: `Linked List`, `Stack`, `Queue`
- `Non Linear` - data item is connected several other items. they are not organized sequentially. it is possible data item to be connected with more than one data items. `Graph` and `Tree` DS are `non lineaar` DS.

Each of these DS has its own properties and intended to work efficiently in different circumstances. EX: `Graph` works perfectly for maps. `Stack` DS works perfectly when you have back and forward buttons in your app.


`Types of Algortitms`
Algoritms can be classified based on problem they are trying to solve. such as:
`sorting`, `searching` algoritms. or they can be classified based on problem solving approach. We classify algoritms which use similiar problem solving approach. In summary we get various ways the problem can be attacked:

Note: This part is just general descriptions. detailed explanation will be provided per each section.
- `simple recursive algoritms` - this work same way as iterative algoritms, recursion acts as a loop. it calls itself recursively. 
- `divide and conquer algoritms`  - divide the problem into smaller subproblems of the same type and solve this problems recursively. combine the solutions to the subproblems into a solution to the original problem. Traditionally, algoritm is called divide and conquer if it contains at least two reqursive calls. `quick sort` and `merge sort` can be example
- `dynamic programming algorithms`- works based on memoization. It means it remembers past result and use them to find new result. These algoritms are generally used for optimization problems. The goal is to find best solution among multiple solutions.
- `greedy algorithms` - are also for finding the best solutions and work well for optimization problems. a greedy algoritm works in phases. At each phase we take the best way we can without worrying about future consequences, hoping that by choosing local optime solution at each step we will achieve global optime solution for whole problem at the end.
- `brute force algortims` - this algo simply tries all possiblities until a saticifactory solution is found. For instance: finding best path between 2 locations. one way is to try all ways and compare results to find the best one.
- `randomized algoritms` - use a random number at least once during the computation to make a decistion.

## __Recursion__
`Recursion` is a way of solving a problem by having a function calling itself.
In computer science(CS from now on), recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. Such problems can generally be solved by iteration as well.  (Russian doll as example for recursion). Main properties of recursion is:
- performing the same operation multiple times with different inputs
- in every step we try smaller inputs to make problem smaller
- base condition is needed to stop the recursion, otherwise infinite loop will occur. base condition is the one after that we will not do any recursion. 
`Recursion` = a way solving a problem by having a function calling itself.
```python
# code example
def open_russian_doll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        open_russian_doll(doll-1)
```
__`Note:`__ `sys.setrecursionlimit(limit)` Set the maximum depth of the Python interpreter stack to limit. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. 

Why we need recursion? The reasons to learn recursion:

__`Recursive thinking`__ is very important in programming and it helps us to break down big problems into smaller ones and easier to use. If we compare writing code with `recursive` and `iterative(loops)` way we can say that writing recursive code easier. We need to choose then depending on situation. So when we can use recursion. the important point is subproblem must be similiar, otherwise recursion is not a good choice. But how we know subproblem is similiar in nature. If you should solve problem with one of below cases, it is good candidate for recursion:

- if we can divide the problem into similiar subproblems 
- Design an algoritm to compute nth...
- Write code to list n...
- Implement a method to compute all

__`The prominent uage of recustion`__ in data structures like `trees` and `graphs`. So when we deal with trees recursion almost become mandatory to use.

__`Interviews`__ many big companies ask questions related to recursions during the interviews.


__`frequently used`__ It is used in many algorithms.(divide and conquer, greedy and dynamic programming)


__`How recursion works?`__
When we created recursive function we need to take into account two conditions,
a condition where a function calls itself with a smaller values and second condition to exit from an infinite loop.
1. a method calls itself.
2. exit from infinite loop

```python
def recursive_func(parameters):
    if exit from condition saticified:
        return some value
    else:
        recursive_func(modified parameter)
```

```python
def recursive_func(number):
    if number < 1:
      print("smaller than 1")
    else:
      recursive_func(number - 1)
      print(number)

recursive_func(10)
# the output will be from 1 to 10, this is because of Stack Memory last in, first out principe.
```

__`Recursive vs Iterative Solutions`__
Any problem solved with recursion can be solved with iteration.
```python
# recursive and iterative way of finding power of 2 of entered number

def power_of_two_rec(n):
    if n == 0:
        return 1
    else:
        power = power_of_two_rec(n - 1)
        return power * 2

def power_of_two_iter(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i +1
    return power

print(power_of_two_rec(5))
print(power_of_two_iter(5))

# if output seems strange to you try to do different recursion tests and 
# keep stack DS works in mind to understand it well. Last in first out.
```

In recursive function infinite recursion can lead to system crash, but in 
iterative function infinite iteration consume cpu cycle. Also recursion repeatedly invokes the mechanism consequently overhead of method calls. This can be expensive for cpu time and memory space. Recursive algos can be very space inefficient. As we explained each recursive call adds new layer to Stack. So if our algo resources to the depth of n, it uses at least O(n) memory.


| Points  | Recursion  | Iteration  |   |
|---|---|---|---|
| Space efficient | No | Yes  | No stack memory is required in case of iteration  |
| Time efficient  | No | Yes  | in case of recursion system needs more time for pop and push elements to stack memory which makes recursion less time efficient |
| Easy to code  | Yes  | No  |  We use recursion especially in  cases we know that a problem can be devided into similiar subproblems |


__`When use/avoid recursion`__

`When to use:`
- when we can easily breakdown a problem into subproblem
- when we are fine with extra overhead(both time and space) that comes with it
- when we need a quick working solution instead of efficient one
- when traverse a tree 
- when we use memoization in recursion

`when avoid it:`
- if time and space complexity matters for us
- recursion uses more memory. if we use embedded memeory. ex: app that takes more memory in the phone is not efficient
- recursion can be slow


`How to write recursion in 3 steps`
Recursion function calls itself repeatidly until base condition is satisified.Function that calls itself is dangerous and should be treated with caution.

`Factorial example:`
Factorial is:
- It is the product of all positive integers less than or equal to n
- denoted by n!
- only positive numbers
- 0 != 1

__`Step 1 Recursive Case - the flow`__

<u>example 1:</u>

If we want to calculate factorial of 4, the answer will be:
4! = 4 * 3 * 2 * 1=24       
but how we got this. it is all positive numbers less or equal to n.
(here 4, so numbers are 4,3,2,1)

<u>example 2:</u>

if want to calculate factorial 10 it will be:

>10! = 10 * 9 * 8 * 7  * 6 * 5  * 4  * 3 * 3  * 2 * 1 = 3628800

based on above we can find factorial n like this
> n! = n * (n - 1) * (n - 2) * ... * 2 * 1

If we pay attention we can write underlined part as  `(n-1)!`
> n! = n * <ins>(n - 1) * (n - 2) * ... * 2 * 1</ins>

let us write it to make this clear
> (n-1)! = (n-1) * (n-1-1) * (n-1-2-) *... *2 * 1 = (n-1) * (n-2) * (n-3) *...* 2 * 1

now it means we can write our function shortly like this
> n! = n * (n-1)!

In this case we found recursive case. let us write this case in code.
```python
# our function for  n! = n * (n-1)! expression
def factorial(n):
    print(n)    # we add this temporaily to understand what is going on.
    return n * factorial(n-1)

# we have developed recursive case(step1) in python
```
Out factorial calculation is almost done. We can say this function is enough for factorial, but this func has a bug. let us run this func.
```bash
python3 factorial.py
...
RecursionError: maximum recursion depth exceeded while calling a Python object

# we will get maximum recursion depth exceeded error. 
```
This means we have limits to keep recurstion funcs in memory. we can increase this limit as below.
```python
import sys
sys.setrecursionlimit(10000)
```
but our purpose is to prevent such case without increasing limit. because if we check output we will see our function keeps calling itself without stopping. if we have such case in application it will lead to crash. We impement this(prevent such case) in step 2.

__`Step 2  Base case - the stopping criteria`__
We need base case to prevent infinite loop. when base case meets function will stop calling itself. We know below expression are true:
```
0! = 1
1! = 1
```
Now let us write base condition in our function
```python
def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial2(n-1)
```

__`Step 3 Unintentional case - the constraint`__

one of important things to consider when writing recursive function is to make sure that function will stop for every possible argument. Now in this phase we need to find in which case our function doesnt stop. In our case function will reach a base case only if n is a non negative integer. We know that factorial is calculated for posituve numbers. Now if we pass negative number to our factorial function we will get max recursion depth error. We 
We need to prevent this case also. There are many ways to achieve this, but we will use simple assertion method which throw an error if n is a non negative number. we can check like this:
> assert n>=0 and int(n) == n, 'the number must be positive integer'
final factorial func will be like this:
```python
def factorial2(n):
    assert n >= 1 and int(n) == n, 'number must be positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial2(n-1)
```
Now if we enter negative or float number as argument we will get error.

### __`Fibonacci numbers -  Recursion`__
We will use above exlained 3 steps to create recursive function to calculate fibonacci numbers. `Fibonacci sequence` is a sequence of a numbers in which each number is sum of the two preceding ones and the sequence starts from 0 and 1. Ex:
> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89....

`step 1 - recursive case`

> f(n) = f(n-1) + f(n-2)     

```python
def fibonacci(n):
    return fibonacci(n-1) + finonacci(n-2)

finbonacci(5)       # but this function will return error saying max 
                    # recursion depth exceeded because we dont have base 
                    # condition
```

`step 2 - base condition`

we know that fibonacci of 0 is 0 and fibonacci of 1 is 1. so we can use this as base class.
```python
def fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

`step 3 - unintentional case - the constraint`

here we also need check negative and float numbers
- fibonacc(-3)      ??
- fibonacci(3.3)    ??

```python
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'fibonacci number can not be negative or non integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

### __`Recursion interview questions`__
1. How to find the `sum of digits of a positive integer number` using recursion ?

```
10   10/10 = 1 and remainder = 0
54   50/10 = 5 and remainder = 4
112  112/10 = 11 and remainder = 1
     11/10 = 1 and remainder = 1
```
> f(n) = n%10 + f(n/10)

```python
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'only positive numbers'
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_of_digits(n//10)
```

2. How to calculate `power of number` using recursion ?

2.1 Recursive case

> x<sup>n</sup> = x * x * x * ..(n times).. * x

2<sup>4</sup> = 2 * 2 * 2 * 2  # if base is same we can write like this
>x<sup>a</sup> * x<sup>b</sup> = x<sup>a+b</sup>

>2<sup>3</sup> * 2<sup>4</sup> = 2<sup>3+4</sup>

We can write out expression like this
>x<sup>n</sup> = x * x<sup>n-1</sup>

2.2 Base case - stopping criterion. as we know
>n<sup>0</sup> = 1

>n<sup>1</sup> = n

And we will use this as base condition, when n reaches 0 or 1 we we return 0 or 1.

2.3 Unintentional case - the constraint

we will pass negative and float numbers as argument for base and exp and check result. based on fails we write assert in our function.

```python
def power_of_number(base, exp):
    assert exp>=0 and int(exp) == exp, 'the exponent must be positive number'
    if exp == 0:
        return 0
    if exp == 1:
        return base
    else:
        return base * power_of_number(base, exp-1)
```

3. How to find `GCD(Greatest Common Divisor) of two numbers` using recursion?

`3.1.`  Recursive case - the flow

GCD is largest positive integer that divides numbers without remainder.
> gcd(8, 12) = 4

How we find this? One way to find this to find prime factorization of two numbers.
```
8 = 2 * 2 * 2
12 = 2 * 2 * 3
```
Here if we take overlapping numbers from both it is 2*2. So gcd is 2 * 2 = 4

Another methods is `Euclidean algoritm` 
```
gcd(48, 18)
step1: 48 / 18 = 2 remainder 12 
step2: 18 / 12 = 1 remainder 6
step3: 12 / 6 =  2 remainder 0
```
If we pay attention we can see recursion. On every step we see second number(18) becomes first and remainder becomes second.

based on above we can write it like below forms
```
gcd(a, 0) = a
gcd(a, b) = gcd(b, a mod b)
```

Now let us write our function.
```python
def gcd(a. b):
    return gcd(b, a%b)
```
If we run function ex: `gcd(48, 18)`  we will get ZeroDivisionError error.

`3.2.` Base case - stopping cretetion

- b = 0

We can take `gcd(a, 0) = a` and write it as our Base condition
```python
def gcd(a. b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
```
If we run this now as `gcd(48, 12)` we will get 6 which is correct.

`3.3.` Unintentional case - the constraint
- Positive integers
- Convert negative numbers to positive

Our final function will be like
```python
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'the numbers must be integer only'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```


4. How to convert a number from `decimal` to a `binary` using recursion
`4.1.`  Recursive case - the flow
1. devide number by 2
2. get the integer quotinent for the next iteration
3. get the remainder for binary digit
4. repeat the steps until quotinent is equal to 0

Let us see example based on number 13. (13 to binary conversion)

| Division by  | Quotinent  | Remainder  |
|---|---|---|
| 13/2 | 6 | 1  |
| 6/2 | 3 | 0  |  
| 3/2 | 2 | 1  | 
| 1/2 | 0 | 1  | 

We repeat steps until we reach 0 as quotinent. Binary number will be as
`1101` from back to forward. Let us see another example:

| Division by  | Quotinent  | Remainder  |
|---|---|---|
| 10/2 | 5 | 0  |
| 5/2 | 2 | 1  |  
| 2/2 | 1 | 0  | 
| 1/2 | 0 | 1  | 

we get binary number `1010`. This is how we convert decimal to binary. But we need to find recursive case. Without recursive case we can not develop recursive function.

In order to formalize recursive func from above table we can write it from bottom to top like:
1010
```
1 * 10 + 0 = 10
10 * 10 + 1 = 101
101 * 10 + 0 = 1010
```
And we can write it like `f(n) = n mod 2 + 10 * f(n/2)`


```python
def decimal_to_binary(n):
    return n % 2 + 10 * decimal_to_binary(n/2)

```


## __`Big O Notation`__
We use `Big O` notation to metric efficiency of algoritms. Without understanding `Big O notation` it is not possible to develop efficient algoritm. If we dont know when our algoritm gets slower or faster it will be hard to judge our program's performance. This consept gives us one way of describing what time our function takes to run grows as the size of input grows. Dependence of function runtime on input size. Example:

```python
# in this example function runtime will get longer depending input size
def digits_sum01(n):
    sum = 0
    for i in range(n):
        sum += i
    return 0


# in this example function runtime will remain same without depening input # size
def digits_sum02(n):
    sum = (n+1) * 10 // 2
    return sum
```

`For ex:` we need send data to our friend daily. We can send data digitally. All will be acceptible if data size is small, but as soon as it gets larger the delivery time will get bigger also. Depending on size this way of delivery may become unacceptible. Another way is to use via transport(plane for ex). In this case the delivery time will remain same not depending on data size.
