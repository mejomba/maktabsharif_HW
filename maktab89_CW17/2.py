import sys

print(sys.argv)
args = sys.argv
if len(args) == 3:
    _, name, famili = args
    print(f'welcome {name} {famili}')
elif len(args) == 4:
    _, name, famili, age = args
    try:
        age = int(age)
        print(f'welcome {name} {famili} {age}')
    except ValueError:
        print('age must be number')