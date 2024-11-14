# while loop is a loop it breaks when conditions gets false
# z=2
# while(z):
#     print("python")
#     z=z-1
n=int(input())
count=0
while(n>0):
    print("the digit is :",n%10)
    n=n//10
    count+=1
print(count)