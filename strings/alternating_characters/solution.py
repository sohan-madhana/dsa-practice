import math
import os
import random
import re
import sys


#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input("Enter number of string inputs you want to enter: ").strip())
    count = 1
    for q_itr in range(q):
        s = input(f"Enter string number {count} :")
        count +=1
        result = alternatingCharacters(s)
        print(f"Result: Number of characters to be deleted for string {s} : {result}")

        # fptr.write(str(result) + '\n')

    # fptr.close()
