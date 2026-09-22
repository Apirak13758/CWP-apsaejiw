import sys
import re
count = 0
if len(sys.argv) > 1: 
    if len(re.findall(sys.argv[1], input("What was the parameter? "), re.IGNORECASE)) > 0:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")