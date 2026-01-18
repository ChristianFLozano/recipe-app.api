def add(x, y):
    return x + y


def substract(x, y):
    return abs(x - y)


def divide(x, y):
    if x == 0 or y == 0:
        return 'Not feasible'

    return x / y
