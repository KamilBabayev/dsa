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

# if output seems strange to you try to do different recursion tests and keep stack DS works in mind to understand it well. Last in first out.
```

