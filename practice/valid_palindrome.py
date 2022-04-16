import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = list(filter(str.isalnum, string.printable))
        def stripper(char):
            if char in alpha_num:
                return True
            return False
        stripped_s = "".join(list(filter(stripper, s)))
        stripped_s = stripped_s.lower()
        lpt = 0
        rpt = len(stripped_s)-1
        if len(stripped_s) == 0:
            return True
        elif len(stripped_s)%2 == 0:
            while stripped_s[lpt] == stripped_s[rpt]:
                if lpt > rpt:
                    return True
                lpt+=1
                rpt-=1
            return False
        else:
            while stripped_s[lpt] == stripped_s[rpt]:
                if lpt == rpt:
                    return True
                lpt+=1
                rpt-=1
            return False           
    def isPalindrome1(self, s):
        newstr=""
        for lt in s:
            if lt.isalnum():
                newstr+=lt.lower()
        return newstr == newstr[::-1]
        # if newstr == newstr[::-1]:
          # return True
        # return False
        

if __name__ == "__main__":
    obji = Solution()
    print(obji.isPalindrome1(s = "A man, a plan, a canal: Panama"))