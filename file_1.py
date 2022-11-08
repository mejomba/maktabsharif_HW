def loop(number):
    print (number)
    if not number:
        return
    if number > 0:
        loop(number - 1)
    else:
        loop(number + 1)
loop(995)