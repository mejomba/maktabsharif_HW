def fibo(x):
    return 1 if x < 2 else fibo(x-1) + fibo(x - 2)
     
    
for i in range(7):
    print(fibo(i))           
