def func1(input_function):
    print(input_function())

def func2():
    return "hello"

func1(func2)
