# string is immutable cannot do any changes to do change so it converted to list
# space complexity : to solve problem we use space there need to be complexity 
# for 2D matrices below n*2
# p a a l e s
s = "apples"
s = list(s)
d = {'a':'p' , 'p':'a'}
for i in range(0, len(s)): # i = 0  
 if (s[i] in d):   # 'a'
   s[i] = d[s[i]]  #s[0]
print(*s)    # or print("".join(s))
