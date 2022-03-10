## Data Structures and Algoritms

Types of Data Structures(DS from now on)). DS can be broadly grouped into 2 basic types:
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