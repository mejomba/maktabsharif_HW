from string import punctuation, ascii_letters, digits
import timeit

value = '1234fd2g1dfg5d6d1g32df1g65dfgdf21g5abc//'


a = '''def func1():
    if any([True for i in value if i in digits]) and \
       any([True for i in value if i in ascii_letters]) and \
       any([True for i in value if i in punctuation]):
        return value'''

b = '''def func2():
    digits_flag = letters_flag = punctuation_flag = False
    for ch in value:
        if ch in digits:
            digits_flag = True
        if ch in ascii_letters:
            letters_flag = True
        if ch in punctuation:
            punctuation_flag = True
    if digits_flag and letters_flag and punctuation_flag:
        return value'''

print(timeit.timeit(a, number=10000000))
print(timeit.timeit(b, number=10000000))