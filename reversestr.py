# input:hello hey world
# output:world hey hello
n=input()
n= n.split(" ")[::-1] #split with space
# print(*n) *  and .join() used to convert list to string
print(" ".join(n)) 
