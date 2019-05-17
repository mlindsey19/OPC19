import sys
x=int( sys.argv[1])
y=1
for _ in range(x):
    for _ in range(x-y+1):
        sys.stdout.write(str(y))
    print''
    y+=1
