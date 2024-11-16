#  input:5 8 9 4 5 5 5 5 8
# output:[5]
nums=list(map(int,input().split())) 
n=len(nums) 
d={} 
for i in nums:
    if(i in d):
        d[i]+=1 
    else:
        d[i]=1 
result=[]
for key,value in d.items():
    if(value > n//3):
        result.append(key) 
print(result)