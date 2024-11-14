# printing highest odd number from the  given string only
s=input()
ind=-1
for i in range(len(s)-1,-1,-1): #(last index,starting index,decrement)
    if(int(s[i])%2==1):         #checking each number odd or not
        ind = i                 #storing odd numbers in a order
        break
result = ""                     
for i in range(0,ind+1):
    result+=s[i] 
print(result)

