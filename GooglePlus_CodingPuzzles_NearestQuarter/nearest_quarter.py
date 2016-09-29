'''
In response to a challenge at https://plus.google.com/u/0/117020778736538274606/posts/GiTCpXZxLdG

"You need to round to the nearest quarter percent.  So if I had 2.11 then it
would round to 2.00, or if I had 1.23 it would round to 1.25, and if you had
3.97 it turns into 4.00."

My solution has been written as a Python doctest.

'''
def nearest_quarter(n):
    """ (number) -> float

    >>> nearest_quarter(1.23)
    1.25
    >>> nearest_quarter(-0.99)
    -1.0
    >>> nearest_quarter(0.375)
    0.5
    >>> nearest_quarter(0)
    0.0
    >>> nearest_quarter(5)
    5.0
    """

    return round (n*4) / 4.0

if __name__ == '__main__':
    import doctest
    print (doctest.testmod())
