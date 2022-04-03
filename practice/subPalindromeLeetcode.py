# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> list:
        result=0
        index=0
        edge_left=0
        edge_right=len(s)-1
        while index < len(s): # abccba
            middle=s[index]
            result+=1
            p1=index-1
            p2=index+1
            self.expand(index-1, index+1, edge_left, edge_right, result, s)
            self.expand(index, index+1, edge_left, edge_right, result, s)           
            index+=1
        print(result)     

    def expand(self, p1, p2, l, r, result, s):        
        while p1 >= l and p2 <= r:
            if s[p1] == s[p2]:
                result+=1
                p1-=1
                p2+=1
            else:
                break        
    def isPalindrome(self, stri):
        "o(n)"
        p1=0
        p2=len(stri)-1
        if len(stri)%2 == 0: # Even input
            while p1 < p2:
                if stri[p1] == stri[p2]:
                    p1+=1
                    p2-=1
                else:
                    return False
            return True
        else: # Odd Input
            while p1 <= p2:
                if stri[p1] == stri[p2]:
                    p1+=1
                    p2-=1
                else:
                    return False
            return True



obji = Solution()
obji.countSubstrings("abc")
obji.countSubstrings("aaa")
obji.countSubstrings("abccba")
# print(obji.isPalindrome("abccba"))
