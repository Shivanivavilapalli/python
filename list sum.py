# input:[1 2 3 3]
# target:5 u have to give one number,from list index is checked to get that number
# output:1 2
def twosum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                return [i,j]
            else:
              return "invalid"
              
nums=list(map(int,input("enter list").split()))
target=int(input("enter your target:"))
print(twosum(nums,target))
            