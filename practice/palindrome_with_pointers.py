def isPalindrome(num):
    "o(n)"
    p1=0
    p2=len(num)-1
    if len(num)%2 == 0: # Even input
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

num1 = "12121" # Odd
num2 = "1221" # Even
num3 = "2333231" 
print(isPalindrome(num1))
print(isPalindrome(num2))
print(isPalindrome(num3))
