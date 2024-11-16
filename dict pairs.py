# input:1 1 2 1 2 3
# output:{1: 3, 2: 2, 3: 1}
# given one list [1,1,2,1,2,3] print dict key value pairs here key=nums value = how mant times number repeated
# output:{1:3,2:2,3:1}
# map = it makes items iterateble
nums=list(map(int,input().split()))
d={}
for i in nums:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1    #d[i]= key number ,1=value no.of items
print(d)
