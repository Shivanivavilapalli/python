# converting lower case to higher case to vice versa
n=input()
u,l=0,0
for i in n:
     if(i.isupper()):
        u+=1
     elif(i.islower()):
        l+=1
if(u>l):
    print(n.upper())
else:
    print(n.lower())