# 1.sum>t:high-=1
# 2.sum<target:low+=1
# enter the list1 1 22 22 33 22 33 223 22
# enter target44
#  output:True
def twoSum(nums,target):
    low = 0 
    high = len(nums)-1 
    while(low<high):
        Sum=nums[low]+nums[high] 
        if(Sum==target):
            return True 
        elif(Sum>target):
            high-=1 
        elif(Sum<target):
            low+=1 
    return False 
nums=list(map(int,input("enter the list:").split())) 
nums.sort() 
target=int(input("enter target:")) 
print(twoSum(nums,target))
            