# Count the number of carry operations required to add two numbers
# https://www.geeksforgeeks.org/count-the-number-of-carry-operations-required-to-add-two-numbers/
# Input: n = 1234, k = 5678
# Output: 2
# 
# 4+8 = 2 and carry 1
# carry+3+7 = carry 1
# carry+2+6 = 9, carry 0
# carry+1+5 = 6
# 
# Input: n = 555, k = 555
# Output: 3

def count_carry(n, k):
    count = 0
    carry = 0
    str_n = str(n)
    str_k = str(k)
    n_pt = len(str_n) - 1
    k_pt = len(str_k) - 1
    res=""
    while n_pt >= 0 or k_pt >= 0:
        if n_pt < 0:
            summ = int(str_k[k_pt]) + carry
        elif k_pt < 0:
            summ = int(str_n[n_pt]) + carry
        else:
            summ = int(str_n[n_pt]) + int(str_k[k_pt]) + carry
        if summ >= 10:
            count +=1
            carry = int(summ/10)
        else:
            carry = 0
        res += str(summ % 10)
        n_pt -= 1
        k_pt -= 1
    res += str(carry)
    return count, int(res[::-1])



print(count_carry(n=1234, k=5678))
print(count_carry(n=555, k=555))
print(count_carry(n=55, k=555))