import sys
if len(sys.argv) > 1: 
    for i in range(0, len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:
    print("none")