# def ispower(x,y):
#     topower = y
#     while y < x :
#         y=y* topower
#         if y == x : 
#             return True
#     return False

def ispower(x,y):
    print(x,y)
    while x !=1 and x > 1 :
        x = x / y
    return True if x == 1 else False

print(ispower(15,2))