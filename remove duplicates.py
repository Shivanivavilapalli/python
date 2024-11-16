# **** remove duplicates from shorted array **
# input:enter the list:1 1 2 2 3 3 4
# output:[1, 2, 3, 4]

# nums = list(map(int,input("enter the list:").split()))
# dups = []
# for i in nums:
#     if(i not in dups):
#         dups.append(i)
# print(dups)


# ****or***
# input:enter the list: 1 1 2 33 33 44 44 5
# output:[1, 2, 33, 44, 5]
nums = list(map(int,input("enter the list:").split()))
i = 0
for j in range(1,len(nums)):
    if(nums[i]!=nums[j]):
        nums[i+1] = nums[j]
        i+=1
print(nums[0:i+1])