import doctest
import sys

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    k = 1
    while k <= n:
        if k % 3 == 0 and k % 5 == 0:
            print("fizzbuzz")
        elif k % 3 == 0 and k % 5 != 0:
            print("fizz") 
        elif k % 5 == 0 and k % 3 != 0:
            print("buzz")
        else:
             print(k)
        k += 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    "*** YOUR CODE HERE ***"
    front = x % 10
    while x // 10 > 0:
        x //= 10
        behind, front = front, x % 10
        if front > behind:
             return False    
    return True


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count, tmp = 1, n % 10 
    while n // 10 != 0: 
        n //= 10
        # print("Debug: n is", n, file=sys.stderr)
        # print("Debug: tmp is", tmp, file=sys.stderr)
        # print("Debug: count is", count, file=sys.stderr)
        if not has_digit(tmp, n % 10):
            count += 1
        if tmp == 0:
            tmp = n % 10 * 10
        else:
            tmp = tmp * 10 + n % 10
    return count 


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    >>> has_digit(132423423, 6)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n != 0:
        if n % 10 == k:
            return True
        n //= 10
    return False


def double(x):
    return x * 2



def triple(x):
    return x * 3

hat = double
double = triple



def team(work):
	return t(work) - 1



def dream(work, s):
	if work(s-2):
		t = not s
	return not t
work, t = 3, abs
team = dream(team, work + 1) and t



def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    end = n % pow(10, t)
    rest = n
    while rest:
        if rest % pow(10, t) != end:
           return False
        rest //= pow(10, t)
    return True
