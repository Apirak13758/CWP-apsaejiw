import sys
import re
if len(sys.argv) > 1: 
    for i in range(0, len(sys.argv)):
        if not re.findall(r"ism", sys.argv[i], re.IGNORECASE):
            print(sys.argv[i]+"ism")
else:
    print("none")