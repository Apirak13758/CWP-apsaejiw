import sys
import re
count = 0
if len(sys.argv) == 3: 
    print(len(re.findall(sys.argv[1], sys.argv[2], re.IGNORECASE)))
else:
    print("none")