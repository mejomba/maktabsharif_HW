nums = ((10,10,10),(30,45,56),(81,80,39),(1,2,3))

# for j in range(len(nums[0])):
#   x = 0
#   for i in nums:
#        x = x + i[j]
#   print(x/len(nums))


for j in range(len(nums[0])): 
  avg = sum(map(lambda x : x[j] ,nums))/len(nums)     
  print(avg)  
