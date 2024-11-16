# input:enter the list:5 0 1 0 2 0 4 0
# output:[5, 1, 2, 4, 0, 0, 0, 0]


# nums = list(map(int,input("enter the list:").split()))
# dups = [0]*len(nums)
# ind = 0
# for i in nums:
#     if(i!=0):
#         dups[ind]=i
#         ind+=1
# print(dups)


#  **** without using built in functions ******

# before code get space complexity
# input:enter the list:1 0 2 0 3 0
# output:[1, 2, 3, 0, 0, 0]
nums = list(map(int,input("enter the list:").split()))
i = -1 # to find where zeros is
for ind in range(0,len(nums)):
    if (nums[ind]==0):
        i = ind 
        break
if(i!=-1):
    for j in range(i+1,len(nums)):
        if(nums[j]!=0):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
print(nums)