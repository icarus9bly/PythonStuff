# Return all subpalindromes in an string:
# s = "aaa" | "a", "a", "a", "aa", "aa", "aaa" | Total: 6
# s = "abc" | "a", "b", "c" | Total: 3

class Solution:
    def countSubstrings(self, s: str) -> list:
        result=[]
        index=0
        edge_left=0
        edge_right=len(s)-1
        while index < len(s): # abccba
            middle=s[index]
            result.append(middle)
            p1=index-1
            p2=index+1
            while p1 >= edge_left and p2 <= edge_right:
                "Expand left and right wrt middle and if touch boundary touch break"
                if s[p1] == s[p2]:
                    result.append(s[p1]+middle+s[p2])
                    p1-=1
                    p2+=1
                else:
                    break
            p3=index
            p4=index+1
            while p3 >= edge_left and p4 <= edge_right:
                if s[p3] == s[p4]:
                    result.append(s[p3]+s[p4])
                    p3-=1
                    p4+=1
                else:
                    break            
            index+=1
        print(result)     

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
