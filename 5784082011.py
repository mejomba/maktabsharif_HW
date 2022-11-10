# def even(nums):
#     print([int(i) for i in nums if int (i) % 2 ==0])


nums = input().split()
# even(nums)

print(list(map(lambda x:x if int(x)%2 == 0 else None ,nums)))