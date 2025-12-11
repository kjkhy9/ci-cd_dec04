import math

def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def div(a,b):
    if b == 0:
        raise ValueError("You cannot divide by 0")
    return (a/b)

def mult(a,b):
    return (a * b)

def sqr(a):
    return a * a

def sqrt(a):
    if a < 0:
        raise ValueError("You cannot find the square root of a negative number")
    return math.sqrt(a)

def log(a, base=math.e):
    if a <= 0:
        raise ValueError("Logarithm input must be greater than 0")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(a, base)

def sin(a):
    return math.sin(a)   # a is in radians

def cos(a):
    return math.cos(a)   # a is in radians

def percentage(a, b):
    if b == 0:
        raise ValueError("Total value cannot be zero for percentage calculation")
    return (a / b) * 100

