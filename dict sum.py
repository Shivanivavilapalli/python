# enter dict:9 -1 85 45 3 -1
# enter target:84
# output:[1, 2]
def twosum(nums,target):
    d={}
    for a in range(0,len(nums)): # a is index nums[a] is a value
        b = target - nums[a]
        if(b in d):
            return [d[b],a]   
        else:
            d[nums[a]]=a   # value with index is stored
nums=list(map(int,input("enter dict:").split()))
target=int(input("enter target:"))
print(twosum(nums,target))

