# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charSet=set()
        res = 0
        for r in range(len(s)):
            curr_r=s[r]
            while curr_r in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res= max(res, r - l + 1)
        return res


obji = Solution()
print(obji.lengthOfLongestSubstring("abcabcbb"))
print(obji.lengthOfLongestSubstring("bbbbb"))
print(obji.lengthOfLongestSubstring("pwwkew"))