def func1(*args):
    for i in args:
        print(i)

my_list = input().split()
func1(*my_list)