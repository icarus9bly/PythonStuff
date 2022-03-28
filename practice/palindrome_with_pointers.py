def isPalindrome(num):
    "o(n)"
    p1=0
    p2=len(num)-1
    if int(num) < 0:
        return False
    elif len(num)%2 == 0: # Even input
        while p1 < p2:
            if num[p1] == num[p2]:
                p1+=1
                p2-=1
            else:
                return False
        return True
    else: # Odd Input
        while p1 <= p2:
            if num[p1] == num[p2]:
                p1+=1
                p2-=1
            else:
                return False
        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        if len(str_x) == 1:
            # If x is one digit number it's palindrome
            return True
        else :
            if str_x == str_x[::-1]:
                # If x as a string is same as mirror image 
                return True
            else:
                return False
            

num1 = "12121" # Odd
num2 = "1221" # Even
num3 = "2333231" 
print(isPalindrome(num1))
print(isPalindrome(num2))
print(isPalindrome(num3))
