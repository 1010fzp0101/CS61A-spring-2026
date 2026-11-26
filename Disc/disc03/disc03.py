"""CS 61A Spring 2026 | Discussion 3: Recursion.

Source: https://lr2933.github.io/cs61a-spring-2026/disc/disc03/index.html
Worksheet: https://lr2933.github.io/cs61a-spring-2026/disc/disc03/disc03.pdf
Student starter file. Fill in the placeholders before running the tests.
"""

from operator import sub, mul


# Q1: Skip Factorial

def skip_factorial(n):
    """Multiply every other positive integer starting at n.

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return skip_factorial(n - 2) * n


# Q2: Swipe
# Use recursion, without while, for, or str.

def swipe(n):
    """Print digits in reverse order, then forward, without repeating the first digit of n.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10)
        print(n % 10)


# Q3: Is Prime
# Assume n > 1. Use a recursive helper instead of a loop.
# Document the helper's behavior.

def is_prime(n):
    """Determine whether n is prime.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(t, n):
        """ Determine whether t is a factor of n """
        if t == n:
            return True
        if t != 1 and n % t == 0:
            return False
        return helper(t + 1, n)
    return helper(1, n)


# Q4: Recursive Hailstone

def hailstone(n):
    """Display the hailstone sequence from n and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)


def even(n):
    return 1 + hailstone(n // 2)


def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1    
    return 1 + hailstone(3 * n + 1)

# Q5: Sevens
# Reverse direction after a multiple of 7 or a number containing 7.

def sevens(n, k):
    """Identify the player who says n in a circle of k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) or i % 7 == 0:
            direction = -1 * direction
        who = (who + direction) % k
        if who == 0:
            return f(i + 1, k, direction)
        else:
            return f(i + 1, who, direction)
    return f(1, 1, 1)


def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)


# Q6: Y combinator (Optional)
# Example: a recursive factorial with a named function.
# >>> fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
# >>> fact(5)
# 120
# Now express factorial as fact = Y(?) without referring to fact in ?.
# Use lambdas, conditionals, calls, mul, sub and equality only.

def Y(f):
    """Fixed-point combinator with deferred recursion."""
    return f(lambda: Y(f))


def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    "*** YOUR CODE HERE ***"
    return Y(lambda g: lambda x: 1 if x == 1 else x * g()(x - 1))  # Replace
