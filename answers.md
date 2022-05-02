# CMPS 2200 Assignment 5
## Answers

**Name:**____Maddie Bonanno_____________________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**

Given N dollars, a greedy algorithm would select the largest possible coin that's less than or equal to N. It continue to iterate, selecting the largest possible coin value and subtracting its' quantity from N, until N = 0.

This algorithm would be optimal because at each step, the algorithm selects the largest coin possible, aka the optimal next choice for producing minimum # of coins that adds to 0. Local optimal solutions leads to the most optimal global solution in this case.

**1b.**

This algorithm has work and span of O(n). Since the greedy algorithm starts with the largest possible coin and values get progressively smaller, there is no overlap. Thus, selecting the proper coins that do not overlap is O(n)




- **2a.**

A counterexample to the previously devised algorithm is as follows:
Let's say you had to exchange 20 USD. The available options are 1, 4, 7, 10, and 14. The greedy algorithm would select 14 first, leaving a value of n = 6. In order to make 20, it would need one 14, one 4, and two 1's, giving a total of 4 coins. However, a nongreedy algorithm would have selected two 10's, which only requires two coins.

The greedy algorithm cannot work because it chooses the largest possible value first. Since there is no guarentee on which coins are available, choosing the largest first will not provide the best option.

**2b.**

A bottom-up memorization approach could be used to solve this problem. Each denomination and powers of the denominations can be saved in a table and the minimum # of coins needed to reach value N can be computed; the algorithm ensures that the next number of coins needed is available (based on entries of table).

The work would be O(k*n) where k is the highest denomination and n is the length of the denomination set (equal to number of nodes). The span is the longest path of the DAG, which is O(n)

***Part 3: Edit Distance
In class we proved an optimal substructure property for the Edit Distance
problem. This allowed us to implement a simple recursive algorithm in Python
that was horribly inefficient. We’re going to implement a slightly different version
of edit distance that includes substitutions, develop an efficient memoization
scheme and then implement a way to visualize the optimal sequence of edits.
3a) The code for MED from the lecture notes is provided as a starting point
in main.py. We will consider a slightly different version of the edit distance
problem which allows for insertions, deletions and substitutions. We will assume
that insertions, deletions and substitutions all have the same unit cost. State
the optimal substructure property for this version of the edit distance problem
and modify MED accordingly.
3b) Now implement fast_MED, a memoized version of MED. Test your implementation code using test_MED.
3c) Now that you have implemented an efficient algorithm for computing edit
distance, let’s turn to the problem of identifying the actual edits between two
sequences.
Notice that in the process of computing the optimal edit distance, we can also
keep track of the actual sequence of edits to each position of S and T. Update
your implementation of fast_MED to return the optimal edit distance as well as
an alignment of the two strings which show the edits that yield this distance.
An alignment just shows what changes are made to S to transform it to T.
For example, suppose S=relevant and T=elephant. If insertion, deletion and
substitution costs are all equal to 1, then the edit distance between S and T is 3
and an alignment of these two strings would look like this:
relev-ant
-elephant
Implement fast_align_MED to return th*** 