import argparse
import operator


op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

parser = argparse.ArgumentParser()

parser.add_argument('num1', type=float)
parser.add_argument('num2', type=float)
parser.add_argument('-o', '--operation',
                    type=str, choices=('+', '-', r'\*', '/'),
                    help=r'for multiplication use \*')

args = parser.parse_args()

print(args)
result = op[args.operation](args.num1, args.num2)
print(result)
