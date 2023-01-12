def reverse_str(string):

    if string == "":
        return string
    else:
        return reverse_str(string[1:]) + string[0]


s = input("input: ")
print(reverse_str(s))