#command line arguments: 1 - input file name; 2 - output file name; 
# 3 - debug printing preferance (1 for on, otherwise off)

import sys

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
if len(sys.argv) > 3:
    debug = int(sys.argv[3])
else:
    debug = 0

def printd(args):
    if debug == 1:
        for arg in args:
            print(arg)

printd([1])