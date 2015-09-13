Title: Permutation(1)
Slug: Permutation algorithm 1 in TAOCP vol.4
Date: 2014/11/28
Tags: Algorithm
Summary: The algorithm that generates all possible permutation for $n$ distinct elements by making just $n!-1$ adjacent interchanges.

__Reference:__ [TAOCP](A book about classical computer science.html) vol.4

The idea is 

* First generate $(n-1)!$ permutation of the $n-1$ elements. And arrange
permutations as a row where the adjacent permutations are related by one
adjacent transposition.
$123\quad 132\quad 312\quad 321\quad 231\quad 213$

* For each permutation, the element of row, we put the $n$-th element in every
possible position from the end and generate a column.
\begin{array}{cccc}
\mathbf{123\underline{4}} &\mathbf{132\underline{4}} &\mathbf{312\underline{4}} &...\\
12\underline{4}3 &13\underline{4}2 &31\underline{4}2 &...\\
1\underline{4}23 &1\underline{4}32 &3\underline{4}12 &...\\
\mathbf{\underline{4}123} &\mathbf{\underline{4}132}
&\mathbf{\underline{4}312} &...
\end{array}
Within each column, adjacent permutations are also related by one adjacent transposition.
Thus we form a grid of square lattice that each site is related to its
nearest-neighbor by one transposition. However, not all transposition are
adjacent transposition, only the elements on the top and bottom rows are related
by adjacent transposition between columns. We can
transverse all permutations by adjacent transpositions by following scheme:
First transverse first column by performing adjacent transpositions
successively. Then, go to the second column horizontally by one adjacent
transposition. By performing successive adjacent transpositions, we will reach the top row
of the second column. Again we can go to the third column horizontally by one
adjacent transposition. Continue this process, we are able to transverse all
permutations with adjacent transpositions only!!



