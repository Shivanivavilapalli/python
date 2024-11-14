# creating  a strong password u=uppercase,l=lowercase,d=numbers,sp=special character
s = input()
u,l,d,sp=0,0,0,0
for i in s:
    if(i.isupper()):
        u+=1
    elif(i.islower()):
        l+=1
    elif(i.isdigit()):
        d+=1
    else:
        sp+=1   
if(len(s)>=8 and u>0 and l>0 and d>0 and sp>0):
    print("strong password")
else:
    if(len(s)==0):
        print("please enter a password")
    else:
        print("weak password")

