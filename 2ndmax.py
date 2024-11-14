# write code without using any built in methods to print second max number in the list
nums = list(map(int,input().split()))
max = nums[0]
for i in nums:
    if(i>max):
        max = i 
smax = float("-inf")
for i in nums:
    if(i>smax and i!=max):
        smax=i
if(smax==float("-inf")):
    print(-1)
else:
    print(smax)