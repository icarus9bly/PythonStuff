# https://leetcode.com/problems/palindrome-number/
def isPalindrome(x: int) -> bool:
	if x<0:
		return False

	inputNum = x
	newNum = 0
	while x>0:
		newNum = newNum * 10 + x%10
		x = x//10
	return newNum == inputNum


print(isPalindrome(454))

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif len(str(x))%2 != 0:
            # No is odd, with one middle number
            len_x=len(str(x))
            middle=int(((len_x/2)+0.5)-1)
            # Traverse from Middle to start
            start=middle-1
            end=middle+1
            part1=''
            part2=''
            while start >= 0 and end <= len_x-1:
                part1=part1+str(x)[start]
                part2=part2+str(x)[end]
                start-=1
                end+=1
            return part1 == part2
        else:
            middle=int(len(str(x))/2-1)
            start=middle
            end=middle+1
            while start >=0 and end <= len(str(x))-1:
                if str(x)[start] != str(x)[end]:
                    return False
                start-=1
                end+=1
            return True

obji=Solution()
print(obji.isPalindrome(1001))
isPalindrome(454)