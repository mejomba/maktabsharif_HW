def fibo(x):
    return 1 if x < 2 else fibo(x-1) + fibo(x - 2)
     
    
for i in range(30):
    print(fibo(i))           


# def fibo(x):
#     fibo_list = [1,1,]
#     for i in range(2,x+2):
#        fibo_list.append(fibo(i-1) + fibo(i - 2)) 
#     print(fibo_list)

# fibo(3)