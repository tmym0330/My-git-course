from msilib.schema import Error


def divide(a, b):
    if b == 0:
        raise Error("divide by 0")
    return a / b

print(divide(10, 7))