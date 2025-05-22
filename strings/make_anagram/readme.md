A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

**Example**


Delete  from  and  from  so that the remaining strings are  and  which are anagrams. This takes  character deletions.

**Function Description**

Complete the makeAnagram function in the editor below.

**_makeAnagram_** has the following parameter(s):

string a: a string

string b: another string

**Returns**

int: the minimum total characters that must be deleted
Input Format

The first line contains a single string, _a_.

The second line contains a single string, _b_.

**Constraints**

The strings  and  consist of lowercase English alphabetic letters, ascii[a-z].

**Sample Input**
 
cde 

abc

**Sample Output**

4

**Explanation**

Delete the following characters from the strings make them anagrams:

Remove _d_ and _e_ from _cde_ to get _c_.

Remove _a_ and _b_ from _abc_ to get _c_.

It takes 4 deletions to make both strings anagrams.