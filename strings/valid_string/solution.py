import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    freq_count = {}
    for f in freq.values():
        if f in freq_count:
            freq_count[f] += 1
        else:
            freq_count[f] = 1

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) == 2:
        keys = list(freq_count.keys())
        f1, f2 = keys[0], keys[1]
        c1, c2 = freq_count[f1], freq_count[f2]

        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"

        if abs(f1 - f2) == 1:
            if (f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1):
                return "YES"

    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    # fptr.write(result + '\n')

    # fptr.close()
