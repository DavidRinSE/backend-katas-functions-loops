#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Big Dave"


def add(x, y):
    return x+y

def multiply(x, y):
    result = 0
    absX = -x if x < 0 else x
    absY = -y if y < 0 else y
    for _ in range(absX):
        result = add(result, absY)
    return result if x > 0 and y > 0 else -result

def power(x, n):
    result = 1
    absX = -x if x < 0 else x
    for _ in range(n):
        result = multiply(result, absX)
    return result if x > 0 else -result

def factorial(x):
    result = 1
    for i in range(x, 1, -1):
        result = multiply(result, i)
    return result

def fibonacci(n):
    fib = [0, 1]
    for _ in range(n-2):
        fib.append(add(fib[-2], fib[-1]))
    return fib[-1]

if __name__ == '__main__':
    print("add(2,4)", add(2, 4))
    print("multiply(6, -8)",multiply(6, -8))
    print("power(2, 8)",power(2, 8))
    print("factorial(4)",factorial(4))
    print("fibonacci(8)",fibonacci(8))
