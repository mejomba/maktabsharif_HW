def even(nums):
    out = [int(i) for i in nums if int (i) % 2 ==0]
    print(out)



nums = input().split()
even(nums)
