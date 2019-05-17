import sys
x=int( sys.argv[1])
y=1
for _ in range(x):
    for _ in range(x-y+1):
        print(y,end='')
    print('')
    y+=1
