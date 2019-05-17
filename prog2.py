import sys
x = sys.argv[1]
vowel=['A','E','I','O','U']
cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
cc= len(cons)
vv = len(vowel)

x = x[:].upper()
e=0
out=''
for c in x:
    if c in vowel:
        i = vowel.index(c)
        out += vowel[(i+1)%vv]
    elif c in cons:
        i = cons.index(c)
        out += cons[(i+1)%cc]
    else:
        e=1
if (e):
    print 'ERROR'
else:
    print out
