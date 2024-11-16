# input:1 3 2 2 3 3 3 3 4
# output:3
# n//2 = 9//2 = 4 ....3 repeat more than 4 times
nums = list(map(int,input().split()))
n=len(nums)
d = {}
for i in nums:
    if (i in d):
        d[i] = d[i]+1
    else:
        d[i]=1
for key,values in d.items():
    if(values>n//2):
        print(key)
        break