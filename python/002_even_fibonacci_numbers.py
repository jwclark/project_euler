# -*- coding: cp1252 -*-
"""
http://projecteuler.net/problem=2

Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fibonacci(a, b, maximum):
    a,b = b, a+b
    if (b > maximum):
        return 0
    if (b % 2 == 0):
        return b + fibonacci(a, b, maximum)
    else:
        return fibonacci(a, b, maximum)
    

if __name__ == '__main__':
    even_sum = fibonacci(0, 1, 4000000)
    print(even_sum)
    