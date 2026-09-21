import sys
def shrink(string):
    return string[:8]
def enlarge(string):
    return string + (8 - len(string)) * "Z"
if len(sys.argv) > 1: 
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) == 8:
            print(sys.argv[i])
        elif len(sys.argv[i]) < 8:
            print(enlarge(sys.argv[i]))
        else:
            print(shrink(sys.argv[i]))
else:
    print("none")