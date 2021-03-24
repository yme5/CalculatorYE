def addition(a, b):
    return a + b


def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c

def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def squaring(a):
    return a * a


def squareroot(a):
    return a ** .5


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot(a)
        return self.result
