# input:ABcd
# output:2 2
n = input()
u,l,d=0,0,0
for i in n:
    # if (ord(i)>=65 and ord(i)<=90):
    if(i.isupper()):
        u+=1
    # elif(ord(i)>=97 and ord(i)<=122):
    elif(i.islower()):
        l+=1
    elif(i.isdigit()):
        d+=1
print(u,l,d)

        

