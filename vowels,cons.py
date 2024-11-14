# s="krsnatejaa" vowel="aeiou"
# no.of vowels=4
# no.of const=6
s=input()
vowel="aeiouAEIOU"
v=0
c=0
for i in s:
    if(i in vowel):
        v+=1
    else:
        c+=1
print("no.of vowels",v)
print("no.of const",c)

