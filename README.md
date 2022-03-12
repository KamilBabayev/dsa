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
