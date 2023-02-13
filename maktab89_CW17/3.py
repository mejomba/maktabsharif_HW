import argparse

parser = argparse.ArgumentParser()

parser.add_argument('name')
parser.add_argument('family')
parser.add_argument('--age', type=int)

args = parser.parse_args()

print(args)
name, family, age = args.name, args.family, args.age

if name and family and age is None:
    print(f'welcome {name} {family}')
else:
    print(f'welcome {name} {family} {age}')
