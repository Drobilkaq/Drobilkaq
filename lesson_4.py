#1
s = input()

cunt = 0
cuntmax = 0

for k in range(len(s)):
    if s[k]=='н':
        cunt+=1
        cuntmax=max(cunt,cuntmax)
    else:
        cunt = 0
        cuntmax = max(cunt,cuntmax)
        
s = s.replace('н','!')

print(cuntmax,s)

#2
s = input()

i1 = s.index('(')
i2 = s.index(')')
print(s[i1+1:i2:])

#3
import re
s = input().lower()
print(re.findall(r'\bа\w+я\b', s))