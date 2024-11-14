
#input:3221sd23
#output:3221
#input:345@87
#output:345
n=input()
# result=""
for i in n:
    if(i.isdigit()):
        # result+=i
        print(i,end="")
    else:
        break
# print(result)