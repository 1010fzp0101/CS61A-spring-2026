"""CS 61A Spring 2026 | Discussion 4: Tree Recursion.

Source: https://lr2933.github.io/cs61a-spring-2026/disc/disc04/index.html
Run tests: python3 -m doctest -v disc04.py

For the list exercises, stick to literals, indexing, concatenation,
len(), and slicing rather than methods such as append().
"""


# Q1: Insect Combinatorics

def paths(m, n):
    """Count paths from (1, 1) to (m, n) using only up and right moves.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1:
        return 1
    if n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)



# Q2: Max Product

def max_product(s):
    """Find the largest product of non-adjacent entries of s (all >= 1).

    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    """
    "*** YOUR CODE HERE ***"
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return s[0]
    if len(s) == 2:
        return max(s[0], s[1])
    if len(s) == 3:
        return max(s[0] * s[2], s[1])
    first_max = s[0] * max_product(s[2:])
    second_max = s[1] * max_product(s[3:])
    return max(first_max, second_max)
        


# Q3: Sum Fun

def sums(n, m):
    """List ordered sequences totaling n, with entries from 1 to m
    and unequal neighboring entries.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []
        return [sums_to_zero]
    result = []
    for k in range(1, m + 1):
        result = result + [[k] + rest for rest in sums(n - k, m) if rest == [] or rest[0] != k]
    return result


# Q4: A Perfect Question (Optional)

def fit(total, n):
    """Check whether exactly n positive squares can add up to total.
    Repeated squares are allowed.

    >>> [fit(4, 1), fit(4, 2), fit(4, 3), fit(4, 4)] # 1*(2*2) for n=1; 4*(1*1) for n=4
    [True, False, False, True]
    >>> [fit(12, n) for n in range(3, 8)] # 3*(2*2), 3*(1*1)+3*3, 4*(1*1)+2*(2*2) 
    [True, True, False, True, False]
    >>> [fit(32, 2), fit(32, 3), fit(32, 4), fit(32, 5)] # 2*(4*4), 3*(1*1)+2*2+5*5
    [True, False, False, True]
    """
    def f(total, n, k):
        if total == 0 and n == 0:
            return True
        elif total < k * k:
            return False
        else:
            return f(total - k * k, n - 1, k) or f(total, n, k + 1)
    return f(total, n, 1)
