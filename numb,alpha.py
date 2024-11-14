# input:243aerty
# output:v=2,c=3,num=3
n=input()
vowels="aeiouAEIOU"
v=0
c=0
num=0
for i in n:
    if (i.isdigit()):
        num+=1  
    elif(i in vowels):
        v+=1
    else:
        c+=1
print(v,c,num)