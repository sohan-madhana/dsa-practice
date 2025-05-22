You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

**Example**

Remove an  at positions  and  to make  in  deletions.

**Function Description**

Complete the alternatingCharacters function in the editor below.

alternatingCharacters has the following parameter(s):

string s: a string

**Returns**

int: the minimum number of deletions required

**Input Format**

The first line contains an integer **_q_**, the number of queries.
The next **_q_** lines each contain a string **_s_** to analyze.

Constraints

Each string  will consist only of characters  and .

**Sample Input**

5

AAAA

BBBBB

ABABABAB

BABABA

AAABBB

**Sample Output**

3

4

0

0

4