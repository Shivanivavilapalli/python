# print missing number from the array
n=int(input("enter size of elements:"))
nums = list(map(int,input("enter numbers:").split()))
s1=(n*(n+1))//2
s2=sum(nums)
print(s1-s2)