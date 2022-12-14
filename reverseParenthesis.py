'''
Given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.

 
Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
 

Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
'''
def reverseParenthesis(s: str)-> str:
    stack = []
    result = ""
    for c in s:
        if c == "(":
            stack.append("")
        elif c == ")":
            reversed_string = stack.popp()[::-1]
            stack[-1] += reversed_string
        else:
            stack[-1] += c            
    return max_sum % (10**9 + 7)