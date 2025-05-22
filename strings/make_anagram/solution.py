import math
import os
import random
import re
import sys


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    freq_a = [0] * 26
    freq_b = [0] * 26

    for char in a:
        freq_a[ord(char) - ord('a')] += 1

    for char in b:
        freq_b[ord(char) - ord('a')] += 1

    deletions = 0
    for i in range(26):
        deletions += abs(freq_a[i] - freq_b[i])
    return deletions


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input("Enter string a : ")
    b = input("Enter string b : ")

    res = makeAnagram(a, b)
    print(f"No. of deletions : {res}")

    # fptr.write(str(res) + '\n')

    # fptr.close()