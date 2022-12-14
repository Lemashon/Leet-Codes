'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLOngestSubstring(Self,s):
        """
        :type sz: str
        :rtype: int
        """
        mapSet = {}
        start, results = 0,0
        
        for end in range(len(s)):
            if s[end] in mapSet:
                start = max(mapSet[s[end]])
                result = max(result, end-start+1)
                mapSet[s[end]] = end + 1
                return result 