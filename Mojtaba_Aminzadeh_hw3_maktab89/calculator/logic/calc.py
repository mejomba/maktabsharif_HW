import operator


op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calculator(*args):
    num1, operator, num2 = args
    result = op[operator](float(num1), float(num2))
    return result
