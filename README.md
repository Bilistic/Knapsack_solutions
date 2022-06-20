0/1 Knapsack Problem

```
Faculty of Engineering and Science
Department of Computer Science
```

```
 This work was done wholly or mainly while in candidature for an undergraduate
degree at Cork Institute of Technology.
 Where any part of this thesis has previously been submitted for a degree or any
other qualification at Cork Institiute of Technology or any other institution, this
has been clearly stated.
 Where I have consulted the published work of others, this is always clearly at-
tributed.
 Where I have quoted from the work of others, the source is always given. With
the exception of such quotations, this project report is entirely my own work.
 I have acknowledged all main sources of help.
 Where the thesis is based on work done by myself jointly with others, I have made
clear exactly what was done by others and what I have contributed myself.
```

#### CORK INSTITUTE OF TECHNOLOGY

Abstract

A comparative study into common algorithm design paradigms aimed towards the 0/1 knapsack problem. Algorithms such as Branch & Bound, Backtracking, Greedy and Generate & Test will be compared based on accuracy, speed, implementation effort and algorithmic complexity. Test results are produced by use of benchmark testing and candidate data sets generated with methods including Weibull distribution and normal distributions....

## Contents


- 1 Introduction List of Tables vii
   - 1.1 Motivation
   - 1.2 Executive Summary
   - 1.3 Contribution
   - 1.4 Structure of This Document
- 2 Background
   - 2.1 Thematic Area within Computer Science
   - 2.2 0/1 Knapsack Problem
   - 2.3 Branch and Bound
   - 2.4 Backtracking
   - 2.5 Greedy
   - 2.6 Generate And Test
   - 2.7 Benchmark
   - 2.8 Weibull Distribution
- 3 Solving the 0/1 Knapsack problem
   - 3.1 Greedy Algorithm
   - 3.2 Generate & Test Algorithm
   - 3.3 Branch and Bound Algorithm
   - 3.4 Backtracking Algorithm
- 4 Data Analysis & Results
   - 4.1 Modeling
   - 4.2 Analysis
   - 4.3 Results
- 5 Review & Conclusion Contents v
   - 5.1 Project Review
   - 5.2 Key Skills
   - 5.3 Conclusion
   - 5.4 Future Work
- Bibliography
- A Links
- 2.1 backtracking List of Figures
- 2.2 small shapes [1]
- 2.3 large shapes [1]
- 4.1 Greedy Algorithms
- 4.2 Greedy Accuracy
- 4.3 Exhaustive search algorithms
- 4.4 Branch & Bound
- 4.5 Branch & Bound - T2


# List of Tables

```
4.1 Results - Greedy Comparison......................... 21
4.2 Results - Complete Comparison........................ 21
4.3 Results - Memory Comparison G & G.................... 23
4.4 B & B - Comparison.............................. 25
```

## Chapter 1

# Introduction

### 1.1 Motivation

Optimization is a huge area in computing as such it is extremely important, its applications are seen the world over and it is almost guaranteed that the studies of this sector have been applied to software you have utilized. As Moores Law comes to an end we look towards alternative methods of gaining increased performance out of our current technology as such one way of achieving this is through optimized code. Obviously this is not my sole driving force behind my motivation for exploration in the sector of optimization but a part of it. My original goal was to achieve a resource management system in the area of electricity consumption. Whilst I have strayed away from this it was purely keeping in lines with the ideas of such a system. Meaning to solve the above problem I imagined it as a knapsack problem, a problem I had previously never encountered and hence this is where my interest begun as I learned during my research of the numerous approaches taken at solving the problem I was struck by how big the problem actually was and how many areas this problem applies to, hence I decided to focus entirely on a comparison of the more basic methods at solving the knapsack problem.

### 1.2 Executive Summary

The Knapsack problem falls under the class of combinatorial optimization problems in which it tries to gain the best possible profit without exceeding the limits of its container. In this project we will conduct an investigation into numerous algorithms used to tackle the most generic 0/1 knapsack problem. Conclusions will be drawn based on algorithm complexity, duration till completion, generated results and programming effort. We will be using a mixture of algorithms, some completing in a reasonable time (Greedy) and those with a worst case time complexity of O(n).

As mentioned previously the project spans from our original problem presented in semester 1. That being the NASA space apps challenge ”You Are My Sunshine”, the challenge in question required participants to generate a tool to help future explorers reliant on solar power plan their daily activities based on power consumption and expected power generation. Whilst we envisioned numerous solutions for this problem we decided to focus entirely upon a sub problem within this challenge. This investigation spanned from the knapsack problem of selecting X amount of tasks to run with Y amount of power with each task having a satisfaction rating and a power rating (consumptionrating). Whilst a solution to this was easy to achieve I found an undiscovered interest in the knapsack problem as such opted to further compare the common approaches to such a problem.

The main goal of the investigation is to present a valid comparison between Branch and Bound, Generate and Test, Backtracking and Greedy where some algorithms will have multiple implementations that have key differences altering performance. Furthermore I have included a secondary goal of developing a platform that can interpret the huge amount of data generated into a format easily understood by all. Whilst the main goal is the investigation and the majority of project focus was spent on this it is important to dedicate time to developing a system that can use this data for all to understand hence the existence of the secondary objective.

### 1.3 Contribution

Referring to the original project I stressed a goal of contributing in some way to technologies utilized in resource management, carrying this goal with me into this new, adapted project I am able to say that on conclusion of the investigation into this are I will be able to recommend various approaches to not just a knapsack problem but various combinatorial optimization problems as well as rank algorithms applicable to such a problem based on complexity, implementation effort, time and accuracy. Whilst

this may seem vastly different to the original goal set of contributing to a sector I now have the knowledge going forward to return to said problem and complete the original target.

### 1.4 Structure of This Document

Document Content is as follows:

Chapter 1: 
Presents the motivation the problem domain and the expected contribution from this
work being accomplished.

Chapter 2:
Presented within this chapter is related work and the relevance of this subject in relation
to Computer Science. it will explore the 0/1 knapsack problem, applicable algorithms
and the differences between them.

Chapter 3: 
Within this chapter we will view implementations of the different algorithms imple-
mented during this investigation. We will view code snippets and break down the im-
plementation of the algorithm.

Chapter 4: 
In this chapter we will review data collected and present models generated from said
data. Further more we will touch on how said data was interpreted and the relevance of
the chosen metrics.

Chapter 5: 
Chapter 5 will draw conclusions from the data viewed in Chapter 4. Whats more is we
touch on skills learned from this process and acknowledge potential future work to be
carried out.


## Chapter 2

# Background

In this area we will explore related work and the relevance of this subject in relation to Computer Science. We will explore the 0/1 knapsack problem, applicable algorithms and the differences between them.

### 2.1 Thematic Area within Computer Science

The knapsack problem, a section in combinatorial optimization of type NP-Complete. Combinatorial optimization is an area in theoretical computer science that consists of finding an a optimal selection of elements (with regard to some criteria) from a finite set. To fully understand the complexity of the knapsack problem we first must understand the class of NP. Any decision based problem with a given answer that can be verified by a polynomial time algorithm fits within an NP-Class. The knapsack problem of which fits into this is assigned the class of NP-Complete, this means it belongs to both NP-Hard and NP. NP-Hard being a problem that is at least as hard as the hardest problem in NP. As a result of this any polynomial solution to such a problem will be able to solve for the whole of NP. A problem X is NP-hard, if there is an NP-complete problem Y, such that Y is reducible to X in polynomial time [2]. all NP-complete problems can be reduced to any NP-hard problem in polynomial time therefore verifying the statement that a solution for an NP-complete problem can solve for all of NP. It is important to stress that since the knapsack problem is that of an NP-Complete problem it is impossible to solve for larger inputs [3].

In order to conduct controlled comparisons of each algorithm implementation we use a benchmark test which will run each algorithm multiple times under different parameters (stress levels). Depending on the range of elements used this benchmark testing will produce vast amount of data to analyze. Furthermore random generation of elements is achieved using a Weibull distribution. Therefor the topics covered within this report include The Knapsack Problem, Weibull and Normal distribution methods and benchmark testing.

### 2.2 0/1 Knapsack Problem

The 0/1 knapsack problem defined as:

```
∑ni=wixi≤ and xi∈ {0,1}
```

First identified in print in 1957 by George Dantzig[4] a founding developer of linear programming and with earlier roots dating back to 1897 in the early works of mathematician Tobias Dantzig[5]. The knapsack problem is one of the fundamental combinatorial optimization problems, the objective of the problem is to find the best possible solution from numerous other solutions with restrictions set as the capacity of the parent container ”the knapsack”. In general the knapsack is a bin-packing problem, in which the goal is to maximize the total value of items in (typically) a single bin [6]. The specific variant of the knapsack problem we will be using is that of a 0/1 problem, this indicates that for any given element we can either take it 1 or leave it 0. This is oppose to the fractional knapsack problem where we are permitted to brake elements up in order to maximize the volume given in our parent container. Further alternatives include Multi-objective knapsack problems upon which consist more than one constraint and the Multi-dimensional
knapsack problem upon which there is more than one heuristic for each element. More than just the use of sorting elements into a knapsack, the knapsack problem is used and has been used across a vast area of computer science. Common uses include but are not limited to shipping container management, stock management, portfolio optimization, resource optimization and even cryptography whats further is that the knapsack problem often occurs as a sub problem of more complex mathematical models. In the world of cryptography the early works of public key encryption was solved by the use of the ”Merkle Hellman knapsack cryptosystem” (later proven inefficient). This acts as a good example for the problems diversity in that the MerkleHellman system is based on the subset sum problem which happens to be an unusual case of the knapsack problem [7].

Due to the time complexity related to the larger knapsack problems (exponential based on element count) it is practically impossible with given methods to arrive at a verified global optimum as such we must consider what is ”good enough”. Of course this is completely ubiquitous to the individual or application. It really does come down to how badly you need the absolute global optimum for your problem, meaning how long are you willing to wait, how much resources are you willing to dedicate and of course how much are you willing to pay. For example if you are packing a car for a trip and you have 100 items with X amount of weight to carry, it is not necessary for you to know the perfect solution, simply acquiring something that is close to this is adequate. However, similarly this method of thinking might not be applied to a shipping company who wish to organize what containers to place on a ship heading from China to America. In this scenario a company could be loosing thousands in profit by delaying a shipment as such we would like the best possible solution as to maximize company profits. This is the difference between an algorithm providing a local optimum solution and a global optimum solution. Local optimum algorithms such as Greedy often solving the KP 0-1 in reasonable time complexity with a worst case scenario of O(N), oppose to global optimum algorithms such as Branch and Bound finding solutions with a worst case time complexity of O(2n).

### 2.3 Branch and Bound

A Branch and bound algorithm is an evolution of the most simplistic Brute Force approach to solving the knapsack problem. Originally proposed in 1960 by A. H. Land and A. G. Doig for discrete programming it has since been adopted to become the most common approach at solving an NP-Hard problem. As mentioned Branch and Bound came as an improvement over Brute Force to be more specific it was an improvement on Backtracking in turn being an improvement on exhaustive search [8]. Branch and Bound operates on the basis of recursively splitting the search space into a smaller sub space each time re-evaluating the bound, when unsatisfactory bounds are found the algorithm will essentially ”prune” the branch from the search space. This has the ability of removing candidate solutions that it can prove does not contain the global optimum. As such the algorithm is considered constructive in nature, repeating the branching process constructing smaller and smaller subsets/trees until a feasible solution is found [9]. Whilst the method Branch and Bound utilized can find an optimal solution relatively quickly it still has a worst case scenario of evaluating every branch in the tree as such its worst case time complexity is O(2n). Whilst the Branch & Bound algorithm alone can find a solution in a reasonable amount of time for smaller node counts it can be optimized by sorting data during pre processing tasks, depending on the sorting algorithm used this further increases time spent solving during this method. An example of this is utilizing the Timsort algorithm default to Python. This derives from a merge sort algorithm as such shares a worst case complexity of O(NlogN) [10]. This means actual complexity of our Branch & Bound and many other algorithmic functions once implemented are in reality O(NlogN) + (algorithmic complexity) or in this case O(NlogN) + O(2n).

A skeleton of the branch and bound algorithm implemented is as follows:

Bounding function G
Evaluation function X -> using a heuristic
Best solution B
1 - Initialize an empty queue to append candidates to (append an empty element)
2 - loop until the queue is empty.
1 - Take a Node N off the queue
2 - if X(N) > B then B <- X(N)
3 - if G(N) > B then branch on N producing N_i

### 2.4 Backtracking

Backtracking is a general algorithm often applied to constraint satisfaction problems, it offers a convenient method of parsing problems such as the knapsack problem. Coined by American mathematician D. H. Lehmer in the 1950s, Backtracking as mentioned above was an improvement on the common exhaustive search (Brute force) algorithm [11]. Backtracking is an exhaustive algorithm by nature as such like brute force and Branch and Bound its worst case scenario is that it will search every node in the search space. It operates by traversing the tree from the root down in a depth first order, at each node the algorithm will check if the node can be added to provide a valid solution. If this is not the case all sub nodes of this node are removed else this cycle continues to the nodes sub nodes and so on until a leaf is reached (limit) at which point we backtrack up the tree and try an alternative node. Essentially when reaching a node which cant represent a partial solution, the algorithm backtracks by removing the trailing value from the solution, and then proceeds by trying to extend the solution with alternative values [11].

A skeleton of the Backtracking algorithm implemented as follows:

Evaluation function X -> using a heuristic
Best solution B
1 - loop until exhaustion.
1 - take Node N
2 - if X(N) > B then B <- X(N)
3 - B <- recursive call to ./1 using N as the parent.
4 - return B

```
Figure 2.1:backtracking
```
### 2.5 Greedy

A Greedy algorithm is a straight forward design technique that provides a feasible solution that might be the global optimum however the answer will be unverified. It makes decisions based on the next element maximizing or minimizing the total value of all elements selected thus far. As such it can be said to make sub optimum decisions in order to potentially arrive at an optimum result [12]. The knapsack problem can be solved by many variations of the Greedy algorithm. Whilst unable to provide the global optimum Greedy algorithms are still often used as they provide close approximations to the global optimum in a time that most complete algorithms cannot come close to, as such we sacrifice accuracy for time or in large set problems, feasibility.

Due to the Greedy algorithms short sighted approach, set structure will often play a role in the execution time of the function as well as accuracy achieved. As such for most problems it is important to order the set based on the measuring heuristic. In the case of a Greedy algorithm being implemented to solve the 0/1 Knapsack problem we can sort by three heuristics, value, weight and the value in relation to the weight. The third often providing the best approach towards the knapsack problem. In this report we will investigate all three approaches. Essentially the approach consists of a consecutive selection of items with the largest selected heuristic as long as the knapsack capacity admits it. The resulting solution initially starts with value 0 and adds to this on each iteration finishing when the sum of the weights is equal to that of the knapsack capacity or the remaining weight can no longer be filled with the remaining nodes [13].

Sorting by measuring heuristic is of particular importance for concern with the accuracy of your result this is due to the nature of the Greedy algorithm making commitments to certain choices too early which prevent them from finding the best overall solution later, as such we give the algorithm the elements being the highest ranked by heuristic first.

The complexity of a Greedy algorithm is O(N) however, due to the nature of greedy requiring the candidate set to be sorted prior to selection we must account for this. As mentioned above most major sorting algorithms have a worst case time complexity of O(NlogN) as such greedy is presented as O(NlogN) + O(N) = O(NlogN) [14].

A skeleton of the Greedy algorithm implementation as follows:
feasibility function X -> using a heuristic
Solution B
1 - Order the candidate set in relation to the selected heuristic.
2 - for Node N in Ordered set.
1 - if X(N) is True then B append N
3 - Return B

### 2.6 Generate And Test

Often used in relation to artificial intelligence Generate and test provides a method of finding the global optimum solution by creating X amount of sets then testing these sets according to some fitness or objective function removing bad sets, essentially pruning our set of sets. As with exhaustive search based algorithms generate and test given a finite set will always find the global optimum. However, whilst the methodology of generate and test works it is flawed by the complexity of larger problems. In terms of the knapsack problem we work on the super-set of the candidate set, this means that given a candidate set of X elements we have a super-set of 2X. The exponential nature of this means as X becomes larger this algorithm quickly becomes intractable. Also known as combinatorial explosion an example would be a candidate set of size 30 giving us 2^30 = 1073741824 permutations to consider, by adding 5 elements we now have 34359738368 permutations a significant difference. An alternative to running the entire subset is to simply not generate the subset by eliminating the known unfeasible solutions prior to assessment via a fitness function.

A skeleton of the Generate And Test algorithm implementation as follows:
1 - Generate your candidate data sets
2 - Order datasets based on the sum of the value of all nodes within the dataset
3 - Return the head of your candidate data set.

### 2.7 Benchmark

In order to assess the performance of each algorithm as well as different implementations of the algorithms we must run them in a controlled series of tests, these tests will increase load through a series of iterations altering one variable at a time. Bench-marking will help us assess the speed and accuracy of algorithms under various loads. The benchmark test implemented comprises of 3 variables, node count, shape and capacity. Throughout testing, candidate sets are made from randomly generated nodes these nodes are made through two different distribution designs, Weibull distribution and normal distribution (more on these later) for the purposes of the benchmark a Weibull distribution is utilized. The weibull parameters for the benchmark allow for one scale and a shape from the set [0.5, 1.5, 5], node counts include a set ranging from 3 - 100 and capacity ranges from a set of [70, 50, 30] each representing a percentage of the total weight of all nodes in the generated candidate set. This is repeated multiple times in order to get the average result for each metric this also serves a smoothing effect as some tests may contain abnormalities resulting in bumpiness when represented on graphs.

Taking from the above the benchmark test implemented can be seen as follows:
Node_count set X
Shape Y
Scale_set Z
Capacity_set I
1 - For amount x in X
1 - create candidate node set N
2 - For Scale z in Z
1 - initialize node values in N with scale z and shape Y
2 - For capacity i in I
1 - capacity = sum(N->weights )/100*i
2 - Run algorithms
3 - Log data

### 2.8 Weibull Distribution

The Weibull distribution is a continuous probability distribution within probability theory. Named after Swedish mathematician Waloddi Weibull thanks to the work accomplished in his paper ”A Statistical Distribution Function of Wide Applicability” published 1951 [15], It has a probability density function defined as the following:

```
∫(χ;λ,κ) = { κλ (χλ)κ− 1−(χ/λ)κ χ≥ 0 , 0 χ≤ 0 ,
```
Whereκ >0 is the shape parameter andλ >0 is the scale parameter of the distribution. The density function utilized changes drastically with the value of k. As seen in figure
2.2 below, the Weibull distribution has the ability to produce vastly different plots based on the shape ’κ’ parameter provided.

```
Figure 2.2:small shapes [1]
```
Figure 2.3 shows how the larger shape parameter distributions have lower spread shown by successively taller density functions centering towards the value of the scale parameter
compared to a larger spread presented within Figure 2.2 [1].

For our purposes of the Weibull distribution we require high diversity in generating candidate elements as such utilization of smaller shape parameters acknowledged within figure 2.2 have satisfied this need. The nature of the highly skewed ranges produced by the shapes presented have given us highly diverse values for use as node weights and node values. In contrast higher shape values would of produced ranges less skewed around the scale parameters as can be seen within figure 2.3. This would of produced nodes with node values closely related to the weight of the node as such a set of nodes with such characteristics would fail to represent the vast diversity of a knapsack problem in the wild. Our parameter based benchmark has been tested with shapes [0.5, 1.5, 5] and held a consistent scale of 1000. These values have been run against set sizes ranging from 3-100 to produce dynamic sets of nodes successfully.

## Chapter 3

# Solving the 0/1 Knapsack problem

In this section we will view implementations of Branch & Bound, Generate & Test, Greedy and backtracking algorithms explored during the course of this investigation.

### 3.1 Greedy Algorithm

Three variants of the Greedy Algorithm have been implemented during this investigation. Greedy ratio oriented, weight oriented and value oriented approaches.

By far the most accurate greedy algorithm mentioned, Greedy ratio oriented operates by calculating the ratio between node weights and node values. It then reorders the set according to the values calculated as to maximize of minimize the value of the solution,following this we then evaluate and add nodes until the parent container is full or we have exhausted all nodes. The implementation of the Greedy algorithm for purposes of this investigation was exclusively in python and can be seen below:

finished_list = dict()
tasks = {x.id: x for x in tasks}
for task in sorted(tasks.values(), key=operator.attrgetter(var), reverse=reverse ):
   if task.value <= capacity:
      finished_list[task.id] = task
      capacity -= task.value
      tasks.pop(task.id)
      if capacity is 0:
         break
return sum(x.satisfaction for x in finished_list.values ())

#### 13

Breaking down the above code to the following steps:

Step 1: order the candidate set in reverse by ratio. This has the effect of ordering from highest value to lowest, ’ratio’ being designated by ’key=operator.attrgetter(var)’.

Step 2: Loop through this new list verifying if the present node is capable of fitting within the parent container ’if task.value <=capacity:’ if so we account for the newly
added item by decreasing the capacity.

Step 3: return either the sum of the values selected or the selected nodes themselves.

Similarly alternative implementations of the Greedy algorithm can be implemented by just altering the sorting heuristic since the underlying algorithm is essentially the same
as such the fully implemented Greedy function is as follows:

def greedy(tasks , capacity , method =0):
var = ""
reverse = True
if method is 0: # Ratio
var = "ratio"
elif method is 1: # Value
var = "satisfaction"
else: # Satisfaction
var = "value"
reverse = False
finished_list = dict()
tasks = {x.id: x for x in tasks}
for task in sorted(tasks.values(), key=operator.attrgetter(var), reverse=reverse ):
if task.value <= capacity:
finished_list[task.id] = task
capacity -= task.value
tasks.pop(task.id)
if capacity is 0:
break
return sum(x.satisfaction for x in finished_list.values ())

### 3.2 Generate & Test Algorithm

Implemented three times within the project the Generate and test algorithm utilized underwent one mutation, version two being implemented in both C++ and Python for speed and memory usage comparisons.

Version one of the generate and test algorithm was implemented solely in Python as such was written in a purely pythonic manor. The basic implementation operates on the basis of taking a candidate set X, generating all permutations for X (The super

set of X) and storing them. Then filtering out permutations that do not fit within the constraints of the parent container, With this reduced list we then get the set that contains the maximum total value (The global optimum) and return this as our solution. This implementation can be seen below coupled with a code explanation.

permutations = sorted ({tuple([tasks[y] for y in range(len(tasks))
if x & (1 << y)]) for x in range (2** len(tasks))}, key=getlen)
permutations = [(x, sum(y.satisfaction for y in x)) for x in permutations
if sum(y.value for y in x) <= capacity]
result = max(permutations , key=lambda item: item [1])
return result [1]

Viewing this code implementation we can see in the initial line we generate our set (permutations) of sets. A subset is generated by looping for the amount of possible combinations that can occur 2n. hence what we our seeing in the above code is that for x we check that each ythbit is set, if so we add the relevant node to this subset. This is achieved by shifting by one 1 creating a bit mask upon which only the ythbit is set this in turn is placed over x via the & operator, if the result is not 0 then the condition was met and the node can be added. we then prune this set of sets as mentioned before and computer the maximum set as our global optimum in line 3.

In order to optimize this approach we needed less sets to choose from as such a degree of validation was integrated into the generation of the sets. this was mainly due to the amount of memory required to hold all subsets of the initial set consider the fact we have 2 nsets to compute and store in memory this grows pretty fast. Due to the integration of functional operations the reformatted implementation took on a C approach to coding.

li = []
for x in range (2** len(tasks )):
xy = []
flag = True
xy_val_sum = 0
xy_sat_sum = 0
for y in range(len(tasks )):
if x \& (1 << y):
if xy_val_sum <= capacity and tasks[y]. value <= capacity:
xy.append(tasks[y])
xy_val_sum += tasks[y].value
xy_sat_sum += tasks[y]. satisfaction
else:
flag = False
break
if flag is True:
li.append ((xy, xy_sat_sum ))
result = max(li, key=lambda item: item [1])
return result [1]

### 3.3 Branch and Bound Algorithm

Branch and bound was implemented in both C++ and Python with the coding effort near same apart from obvious syntactical differences. Unsurprisingly considering its origins the core implementation expresses similarity with that of the iterative backtracking algorithm. The basic concept consists of a state space search tree where every level represents a decision in the solution. Any possible solution follows the rule that it starts at the root and ends at a leaf. The root of the tree represented at level 0 has a state being that of no solution has been achieved, whilst the leaf (A level that has no children) presenting a state of where a solution has been achieved. Their are many methods to traverse a state space search tree the two most common being breath-first and best first, both prevent further searching of a levels children when it becomes clear to further search will result in a less than optimum solution.

Within each node of the state space tree we record the level, cumulative weight, cumulative value and the bound. The bound equals the value computed of any candidate solution from the current nodes subsets taking into account current selected nodes and the remaining size of the parent container. If this value is worst than the current best solution we can consider this path to produce a poor solution as such we can prune this branch.

Where U and V is a node initially set to level -1 and attributes null. With Q representing FIFO queue and tasks organized by a certain heuristic representing a best first approach.

while not q.empty ():
u = q.get()
v.level = u.level + 1
v.satisfaction = u.satisfaction + tasks[v.level]. satisfaction
v.value = u.value + tasks[v.level].value
if v.value <= capacity and v.satisfaction > max_satisfaction:
max_satisfaction = v.satisfaction
v.bound = bound(v, capacity , tasks)
if v.bound > max_satisfaction:
q.put(copy.deepcopy(v))
# not selecting (reset)
v.satisfaction = u.satisfaction
v.value = u.value
v.bound = bound(v, capacity , tasks)
if v.bound > max_satisfaction:
q.put(copy.deepcopy(v))
return max_satisfaction

```
def bound(node , cap , tasks ):
if node.value >= cap:
return 0
sat = node.satisfaction
t_weight = node.value
lvl = node.level+1
while lvl < len(tasks) and (t_weight + tasks[lvl]. value <= cap):
t_weight += tasks[lvl]. value
sat += tasks[lvl]. satisfaction
lvl += 1
if lvl < len(tasks ):
sat += ((cap - t_weight )*( tasks[lvl]. satisfaction/tasks[lvl].value))
return sat
```

### 3.4 Backtracking Algorithm

Backtracking was implemented three times, twice in python providing a comparison of an iterative and recursive approach towards such an algorithm in terms of both speed and implementation complexity. A third time in C++ providing a speed comparison between the algorithm on different code-bases. Backtracking provides a simple approach towards solving the knapsack problem, it takes the core concept of an exhaustive search on a state space tree and simply stops searching the current branch when realizing it has reached the parent containers capacity. It will then proceed to ”backtrack” to the last feasible node and continue down its alternative child this will be done until all feasible nodes have been evaluated.

An iterative version of the backtracking algorithm is presented much alike the implementation seen by Branch and Bound, utilizing a queue to store candidate nodes for later evaluation. The code for this is presented below, preconditions include those mentioned for Branch and Bound. 

while not q.empty ():
u = q.get()
v.level = u.level + 1
v.satisfaction = u.satisfaction + tasks[v.level]. satisfaction
v.value = u.value + tasks[v.level].value
if v.value <= capacity and v.satisfaction > max_satisfaction:
max_satisfaction = v.satisfaction
if v.level != len(tasks )-1:
if v.value <= capacity:
q.put(copy.deepcopy(v))
v.satisfaction = u.satisfaction
v.value = u.value
if v.value <= capacity:
q.put(copy.deepcopy(v))
return max_satisfaction

Alternatively the recursive implementation is as follows:

def backtrack_rec(tasks , cap , opt , max):
if opt.level + 1 is len(tasks ):
if opt.value <= cap and opt.satisfaction > max:
max = opt.satisfaction
else:
u = copy.deepcopy(opt)
opt.level += 1
opt.value = opt.value + tasks[opt.level ]. value
opt.satisfaction = opt.satisfaction + tasks[opt.level ]. satisfaction
if opt.value <= cap and opt.satisfaction > max:
max = opt.satisfaction
if opt.value <= cap:
max = backtrack_rec(tasks , cap , copy.deepcopy(opt), max)
opt.value = u.value
opt.satisfaction = u.satisfaction
if opt.value <= cap:
max = backtrack_rec(tasks , cap , copy.deepcopy(opt), max)
return max

Code aside the logic of a recursive approach is similar in many ways apart from the areas of selecting a node, in an iterative approach candidate nodes are appended to the back of the queue to be evaluated on their turn. However, a recursive approach would see the candidate and all children test first due to the nature of a recursive method call.

## Chapter 4

# Data Analysis & Results

In this chapter we will review data collected and present analytical models generated from said data.

### 4.1 Modeling

When modeling data for Branch & Bound, Generate & Test, Backtracking and Greedy it was important to decide on the metrics of which to measure the efficiency of the algorithms, selected metrics included run time, memory consumption and accuracy. An algorithms worth in relation to the 0/1 knapsack problem can be measure by these three metrics.

Run-time being the most prevalent metric as most graphs presented are mapped as run-time vs node count. Specifically the run-time metric relates to time from algorithm start to result end. However, this value alone does not represent an algorithms run time value, this value is achieved by running the algorithm under many different conditions essentially stress testing the algorithm multiple times in order to gain the average value for a node count. Whilst of the most importance the run time value does not tell the complete story for all algorithms, based on purely this data one could provide results indicating greedy as the best algorithm without considering metric such as accuracy which plays a big part in a greedy algorithm.

Accuracy is concerned with many incomplete algorithms however Greedy was the only algorithm of its kind to be included within this investigation. Accuracy is included as a metric based on the fact we never truly know if the result returned from a greedy algorithm is the global optimum, luckily we can measure this against our exhaustive search algorithms that are guaranteed to return the global optimum.

Memory whilst insignificant as a metric to a Greedy algorithm plays a key role in the downfall on many exhaustive search algorithms. It is the result of the exponential growth in nodes to be represented by a search space tree or power-set in the case of a Generate & Test algorithm as such modeling memory consumption for certain algorithms can reveal what time may not.

### 4.2 Analysis

Our setup includes a previously mentioned benchmark generator part of this process will measure each algorithm based on the above metrics storing the resulting values in an excel friendly format. Depending on node count and passes run data generated can be in the hundreds if not thousands of lines as such manipulation of this data is tedious at best. In order to truly analyze this data and generate graphs as seen within this chapter we designed and utilized a web based platform working with a flask backend. This platform utilizes Pandas library for Python to produce data viable for plotting. Furthermore implementation of this platform allowed for data filtering making it easier to analyze specific results for certain parameters.

### 4.3 Results

Results presented in this section are gathered from algorithms presented in chapter 3, all implemented in Python unless stated otherwise. The test platform consists of an 8 core AMD 8370 running at 4.0GHz with 16GB of RAM, with each algorithm run 9 times for each node count with the result being the average taken from this. Since search space algorithms such as Branch & Bound, Backtracking and Generate & Test have a time complexity of O(2n) making it Unfeasible to calculate optimal solutions for large data sets as such values have been left as ”NA”. However, when utilized in a lower level language the speed and use of less memory allows for these limits to be significantly higher.

```
Table 4.1:Results - Greedy Comparison
size Greedy W Greedy R Greedy V
5 0.000013 0.000013 0.000012
10 0.000022 0.000025 0.000021
20 0.000054 0.000051 0.000033
25 0.000071 0.000095 0.000075
30 0.000059 0.00011 0.000035
40 0.000054 0.000056 0.000046
```
```
Table 4.2:Results - Complete Comparison
size G & T B & B Backtracking
Rec
```
```
Backtracking
Iter
5 0.00012 0.00022 0.0019 0.0010
10 0.006 0.0036 0.070 0.035
20 13.83 0.016 74.32 29.81
30 NA 3.26 NA NA
40 NA 42.11 NA NA
50 NA 700.01 NA NA
```
From the results we can clearly see the exponential nature of exhaustive search based algorithms and how poorly they scale in comparison to incomplete algorithms such as Greedy algorithms. Greedy holding a worst case time complexity of O(N) as such providing solutions in a scale of sub second measurements in comparison to the tens of seconds, minutes and hours taken at different nodes counts of exhaustive search algorithms. In figure 4.1 three different greedy algorithms follow a similar line of best fit around their plotted points, the difference in each being the sorting heuristic between weight, value and ratio. This sorting may be the cause of the time difference between each as the fundamental choosing function is the same for all. Redundant of time between competing Greedy algorithms it is clear they provide far greater scale-ability compared to exhaustive search algorithms.

However, as with most things there comes a trade off, in this case accuracy for time. In figure 4.2 we compare the three different greedy algorithms mentioned in terms of accuracy. this was taken between node range[5,30] with results compared to that achieved of branch and bound and the resulting accuracy being the average of all passes. This means for each node the algorithm was run 9 times the result for this node being the average of the nine, as the same with Branch & Bound and the accuracy tallied. This was achieved for the entire range and as such the final accuracy being the average of the

```
Figure 4.1:Greedy Algorithms
```
```
Figure 4.2: Greedy Accuracy
```
entire range. The results indicate greedy ratio and value (Satisfaction) proved accuracy of over 97% compared to high 60’s for a greedy based weight algorithm. This stands true when tested on a node count of up to 50, indicating greedy algorithms sorted by the correct heuristic provide a ”good enough” solution in the time taken compared to its exhaustive search relatives.

Further examination of exhaustive search algorithms within figure 4.3 prove Generate & Test to be the fastest of a bad bunch. However, whilst an improvement on time Generate & Test utilizes the most amount of memory of all the algorithms tested and as with time, memory consumption proves exponential towards the size of the candidate node set. Measures taken to reduce the amount of potential candidates by pruning the

```
Figure 4.3:Exhaustive search algorithms
```
generated sets have proven successful in lowering memory usage but merely prolong the inevitable as the amount of nodes grow. Table 4.3 will see memory consumption of a C++ implemented Generate & Test algorithm as described above. Unable to complete for node counts above 30 due to the large amount of sets to store, memory consumption equaling 2^30 that being of 1,073,741,824 possible combinations equaling 2147.48mb worth of storage required for solving a mere 30 elements. If this number increases to 35 we now must be able to store 68719.48mb a huge increase over the amount already required to store 30, again due to its exponential nature. It is important to note that the algorithms equal implementation in python could see memory usage three times as high as that presented within table 4.3 due to the large amount of memory used to store python integers.

```
Table 4.3:Results - Memory Comparison G & G
Nodes Memory - MB
10 0.488
15 1.5
20 5.1
25 156.3
30 868.1 - cap
```
Furthermore in figure 4.3 we see the difference in time a recursive backtracking function takes over an iterative one. Whilst the difference becomes greater the higher the node count, an iterative backtracking function is still in-feasible in node counts past 25. However, in larger node counts whilst time is also a factor, as is with Generate & Test

an iterative backtracking approach eventually consumes to large an amount of memory further adding to the in-feasibility of this approach.

```
Figure 4.4:Branch & Bound
```
In figure 4.4 Branch & bound is presented as an unpredictable algorithm peaking randomly, this may be due to the worst case time complexity of a Branch & Bound algorithm being O(2n) and how Branch & Bound operates. As such a best case scenario for this algorithm is it finds a solution within the first branch it looks in, therefor eliminating the remainder. However, worst case provides it will search the entire tree and find the optimal solution in the last branch searched. Keeping this in mind on the tail end of the graph we see a valley like structure appear this may be due to this very reason. The algorithm is finding node level 28 within the first few branches providing a solution faster oppose to its before and after where it has had to partially search the tree. In comparison to backtracking algorithms these partial searches whilst unpleasant for Branch & Bound far outperform results produced by any other exhaustive search algorithm for this amount of nodes.

In an attempt to smooth the presented data in figure 4.4 the Branch & Bound algorithm was run a further 10 times and averaged however the resulting data produced an even rougher line presented within figure 4.5.

Whilst the results seen so far have been provided with a parent container at capacity that of 75% the sum of node weights, reducing this figure to 30% the sum reveals omething entirely different. Examining the Branch & Bound algorithm working with this restriction we are able to far extend the use-ability of the algorithm to over 50 nodes and furthermore reduce the time taken. This is primarily due to finding a solution in less levels of the search space due to the decreased capacity of the parent container.

```
Figure 4.5:Branch & Bound - T2
```
This means we have to consider less nodes than previous tests, this may be improved by deleting nodes with a weight higher than capacity during the sorting of the candidate node set. Table 4.4 presents a comparison of container size and reveals the impact this has.

```
Table 4.4:B & B - Comparison
size 75% 30%
10 0.0036 0.0018
20 0.016 0.0052
30 3.26 0.019
40 42.11 6.41
50 700.01 6.01
```

## Chapter 5

# Review & Conclusion

### 5.1 Project Review

Whilst time was not an issue, goals set during 2018 where not all met. As mentioned in ”Future Work” an online variant of the problem was not investigated within this report. Whilst this was the initial plan I feel we did not fully take into account the complexity behind what was being proposed for the time frame given. Whilst weekly targets where achieved the overall goals was not, this was fully realized half way through the Implementation phase. If this was to occur again greater emphasis must be placed on understanding the problem domain as to not under estimate it again. Whats more is having never utilized C++ and having minimum experience in C I decided to utilize Python as the main language. However, upon implementing the first algorithm in C++ I immediately recognized my mistake in not doing the whole project within C++. This had two meanings, whilst I do regret not starting in C++ without the approach I took I would never of found memory and speed performance differences between the two languages.

### 5.2 Key Skills

From completing this project I feel I have come into contact with only a small portion of what combinatorial optimization has to offer. I have learned algorithm designs I never
knew existed and whilst there are papers out there presenting similar data to what is presented within this report it felt correct to not use this and produce my own. As a result ideas have come to fruition from just understanding the problem domain more clearly than I ever could by just reading about it. Areas never heard of nor explored have come to my attention such as NP and its child categories and whilst my knowledge on these areas has only just scraped the surface it has revealed an interest to understand this sector more so than when i started this project in 2017. Whilst time was a limitation I feel it was well managed setting goals each week worked well and adjusted fine to the change in direction with the project from our initial path to where it is now. Whilst my new found knowledge on optimization is the clear biggest skill achieved from the time spent it would be remiss of me to not mention the experience I have gained spending time programming in C++ and Python previously very little attention given to either language over the past 4 years. The difference between both clearly showed the effects such a high level language has in terms of memory and execution oppose to a low level alternative like C++

### 5.3 Conclusion

Greedy, Branch & Bound, Generate & Test and Backtracking algorithms have been presented within this comparative study. In chapter 4 we viewed the effectiveness of each algorithm and found that whilst the complexity of each is known the approach and heuristics of each problem makes some more suitable than others. We can conclude that whilst the use of exhaustive search algorithms is significantly slower than that of Greedy or Incomplete solutions they offer a significant advantage by delivering the global optimum.

We have shown that algorithm use cases not only should be decided upon node count but that container capacity also makes a significant difference in an algorithms performance for problems wishing to be solved via a complete solution. We considered containers of 75% capacity and that of 30% capacity the difference being that of offering solutions in times incomparable to that of its larger container counterpart as well as extended range in node counts due primarily to the search depth required by smaller containers. This seems to only become a concern with search space algorithms as complexity grows exponentially with regards to node count unlike greedy where a worst case scenario sees it iterate for the amount of nodes therefor the parent container having less of a impact.

Of the three Greedy approaches explored we have shown that accuracy is directly related to that of the sorting heuristic. We explored sorting via ratio, weight and value of hich ratio and value offering us the highest accuracy by a difference of 30% compared to weight. Sorting not only effects Greedy approaches but that of exhaustive search, specifically utilizing a Branch & Bound algorithm upon a sorted set using a ratio heuristic will provide the global optimum in that of less time compared to a weight sorted Branch & Bound approach. This is due to in a manor ”highlighting” candidate nodes by placing them within a higher level on the search space tree.

Furthermore, implementation of greedy algorithms provide a level of difficulty far less than its alternatives. The core concept of the greedy algorithm is easily comprehensible compared to Branch & Bound and equally less in terms of implementation compared to any of the mentioned exhaustive search based algorithms.

Algorithms implemented in C++ out performed Python counter parts by a large margin in terms of speed and memory consumption for all algorithms this in part is directly due to the high level nature of python. Generate & Test originally written in python in a pythonic manor utilizing methods such as list comprehensions meant code executed faster compared to a traditional for loop, primarily due to less overhead of list look ups and appenditure. Whilst this may seem minuscule when micro factors such as this occur on algorithms with complexity O(2n) they begin to add up presenting themselves in times that become infeasible over large data-sets. A re-written version of this in a c++ manner utilizing traditional for loops saw execution time slow due to the added overhead but gave greater control over candidate filtering allowing the implementation to support a greater node count. The same implementation in C++ saw this node count extend even further as memory and speed improved, In python integers are represented by an object taking up three times as much memory as a C integer meaning any implementation in C++ would ultimately require far less memory.

The worst execution time is that of backtracking due to its exponential nature and significant lack of optimization compared to Branch & Bound. Greedy holding the title of best execution time even if offering a solution unverified as the global optimum. This must still be considered as a best fit algorithm for any large node count, more so when we are dealing with nodes in the hundreds. Whilst Branch & Bound boasts impressive times compared to alternative exhaustive search algorithms it places extreme importance on data-set ordering to achieve a solution in a feasible time frame. The uncertainty that you may get stuck searching the entire search space tree on a large node count provokes thought that greedy may be a more suitable alternative for achieving safety and speed at the cost of losing a percentage of accuracy. However, as results presented this loss of accuracy can be minimized by utilizing either value or ratio heuristics to achieve levels of accuracy above 95% the majority of the time.

### 5.4 Future Work

For Future work I would like to see the difference a Genetic algorithm provides compared to our Greedy implementations above. I would also see exploration into an online variant of our knapsack problem, this would see the problem become far more complex as we introduce factors such as replenishing storage and dynamic node values when placed in a time series environment. This would bring the work achieved in this report closer to and more relative to the original problem of energy management. It would also add a level to the problem previously never explored, whilst this was the original goal time constraints restricted us to looking at the basic knapsack problem which in turn provides a conundrum within itself. Whats more is investigation into techniques such as divide and conquer in relation to parallel programming and the implications this has on the 0/1 knapsack program for both online and offline variants could potential see the usability of complete solutions such as Generate & Test and Branch & Bound extended far beyond the results present within this report.


## Bibliography

```
[1] M. D. C. Ignacio Castieiras and B. O’Sullivan, “Weibull-based benchmarks for bin
packing.”
[2] “What are the differences between np, np-complete and np-
hard.” [Online]. Available: https://stackoverflow.com/questions/1857244/
what-are-the-differences-between-np-np-complete-and-np-hard
[3] D. S. Maya Hristakeva, “Different approaches to solve the 0/1 knapsack
problem,” 2005. [Online]. Available: http://www.micsymposium.org/mics2005/
papers/paper102.pdf
[4] I. John J. Bartholdi,The Knapsack Problem: Georgia Institute of Technology.
[5] T. Dantzig,Numbers: The Language of Science, 1930.
[6] “Google optimization tools.” [Online]. Available: https://developers.google.com/
optimization/
[7] R. Alhassawi, “Cryptanalysis of a knapsack cryptosystem,” 2013. [Online].
Available: https://unbscholar.lib.unb.ca/islandora/object/unbscholar%3A7040/
datastream/PDF/view
[8] GeekforGeeks, “Branch and bound — set 1 (introduction with
0/1 knapsack).” [Online]. Available: https://www.geeksforgeeks.org/
branch-and-bound-set-1-introduction-with-01-knapsack/
[9] P. J. KOLESAR, “A branch and bound algorithm for the knapsack
problem.” [Online]. Available: https://www0.gsb.columbia.edu/mygsb/faculty/
research/pubfiles/4407/kolesarbranchbound.pdf
```
[10] “Merge sort.” [Online]. Available: https://www.geeksforgeeks.org/merge-sort/

[11] T. W. Francesca Rossi, Peter Van Beek, “Constraint satisfac-
tion: An emerging paradigm,” Handbook of Constraint Programming, 2007. [Online]. Available: https://web.archive.org/web/20070317015632/http:
//www.cse.ohio-state.edu/∼gurari/course/cis680/cis680Ch19.html#QQ1-51-128

[12] P. E. Black, “greedy algorithm,” Dictionary of Algorithms and Data Structures
[online], February 2005. [Online]. Available: https://www.nist.gov/dads/HTML/
greedyalgo.html

[13] A. K. Gennady Diubin, “The average behaviour of greedy algorithms for the knap-
sack problem: General distributions,” 2003.

[14] A. Shaheen and A. Sleit, “Comparing between different approaches to solve the
0/1 knapsack problem,”IJCSNS International Journal of Computer Science and
Network Security, July 2016.

[15] W. WEIBULL, “A statistical distribution function of wide applicability,” 1951.


Appendix A

## A Links

Data Visualization platform https://www.youtube.com/watch?v=QfuucuVt8vcfeature=youtu.be



