nums = ((1,2,3,5),(20,12,11,6),(11,24,2,1))



# for j in range(len(nums[0])):
#   x = 0  
#   for i in nums: 
#        x = x + i[j] 
#   print(x/len(nums))     


for j in range(len(nums[0])): 
  avg = sum(map(lambda x : x[j] ,nums))/len(nums)     
  print(avg)  


