# input : [ 1 1 2 2 3]
#         [1 2 3]
# output:[1 1 1 2 2 2 3 3]
# input:enter first list:1 1 2 2 3
# enter second list:1 2 3
# output:[1, 1, 1, 2, 2, 2, 3, 3]
nums1=list(map(int,input("enter first list:").split()))
nums2=list(map(int,input("enter second list:").split()))
nums3 = nums1 + nums2
nums3.sort()
print(nums3)
           