Title: Permutation(0)
Slug: Introduction of permutation in TAOCP vol.1
Date: 2014/06/01
Tags: Algorithm
Summary: Basic notions of permutation. And some convenient representations.

__Reference:__ [TAOCP](A book about classical computer science.html) vol.1

Permutation is a fundamental concepts in combinatorics. Assume we have a multi
set, $\\{ a_{1,1},...a_{1,n_1},a_{2,1},...a_{2,n_2},...a_{N,n_1},...a_{N,n_N} \\}$,
the total number of different ways to arrange them is $\frac{(\sum n_i)!}{\prod
n_i !}$. We will focus on the case $n_i=1$ which is the case of $N$ distinct
objects. And the number of ways to arrange them is $N!$. Later we use perms to
stands for the word permutations.

Perms have several different representations.

* Linear representation
* Cyclic representation
* Canonical representation

## Linear representation

Perm can be considered as a _rearrangement_ or _renaming_ of a series of
objects. Suppose we put five objects $a,b,c,d$ in a straight line. And the perms
which change the ordering into $b,a,d,c$ can be denoted as
\\begin{equation}
\\left(
\\begin{array}{cccc}
a &b &c &d\\\\
b &a &d &c
\\end{array}
\\right)\\equiv
\\left(
\\begin{array}{cccc}
b &a &c &d\\\\
a &b &d &c
\\end{array}
\\right)\\text{.}
\\end{equation}

Note, the expression for linear representation is not unique as we show in the
above equation.

## Cyclic representation

Cyclic representation represents the perms by breaking perms down into closed
cycles. The previous example will be represented by $(a b)(c d)$. Also, this
representation is not unique $(a b)(c d)\equiv(b a)(c d)$. For the object,
$e$, that do not change position is denoted by singleton $(e)$. It is usually
omitted in cyclic representation.

## Canonical representation

The canonical representation can be constructed by following steps.

* Write all singleton cycles explicitly.
* Within each cycle put the _smallest_ number _first_.
* Order the cycles in _decreasing_ order of the _first_ number in cycles

It is a faithful representation of perms since it modified the cyclic
representation by ordering the representation within each cycle and between
different cycles(That's why singleton should be included in the representation).

It can also be a faithful representation if in the last step we order the cycles
in __increasing__ order of the _first_ number. The reason we use asymmetric
scheme in second and third step is because the cyclic structure can be encoded
in the series in an elegant way. It is better described by following example.

### Example

Suppose we have a perm in cyclic representation $(3 1 6)(5 4)$. Following the
steps above

* $(3 1 6)(5 4)(2)$
* $(1 6 3)(4 5)(2)$
* $(4 5)(2)(1 6 3)$
	* The parenthesis _can be removed_ without causing any ambiguity.

$452163$ can be restored by inserting $|$ before _left to right_
minimum by following steps:

* 4 is the minimum of 4, insert $|$ before 4.
* 5 is not minimum of 45, do nothing.
* 2 is the minimum of 452, insert $|$ before 2.
* 1 is the minimum of 4521, insert $|$ before 1.
* 6 is not minimum of 45216, do nothing.
* 3 is not minimum of 452163, do nothing.

We will get $|45|2|163$, which is exactly the canonical representation.

The canonical representation has several advantages:

* It is canonical.
* The representation can be implement into computer with less ambiguity.
* The structure of perms can be reformulate into the structure of the _left to right minimum_ of the sequence.

