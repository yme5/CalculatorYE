def addition(a, b):
    a = float(a)
    b = float(b)
    c = b + a
    return c


def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c


def multiplication(a, b):
    a = float(a)
    b = float(b)
    c = b * a
    return c


def division(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    return round(c,9)


def squaring(a):
    a = float(a)
    c = a * a
    return c


def squareroot(a):
    a = float(a)
    c = a ** .50000
    return round(c, 9)


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
