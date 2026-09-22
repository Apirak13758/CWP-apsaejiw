import sys
count = 0
if len(sys.argv) > 1: 
    for i in sys.argv[1]:
        if i == 'z':
            print("z", end="")
            count += 1
    if count == 0:
        print("none")
else:
    print("none")