import sys
x = sys.argv[1]

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
