# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val}"
class Solution:        
    def addTwoNumbers(self, l1, l2):

        head1=l1
        head2=l2
        carry=0
        head3 = None
        while head1 or head2:
            if head1 == None:
                summ = head2.val + carry
                head2=head2.next
            elif head2 == None:
                summ = head1.val + carry
                head1=head1.next
            else:
                summ = head1.val + head2.val + carry
                head1=head1.next
                head2=head2.next                
            if summ >= 10:
                carry = int(summ / 10)
            else:
                carry = 0
            if head3:
                head3.next = ListNode(summ % 10)
                head3=head3.next
            else:
                top = head3 = ListNode(summ % 10)
            print(f'head3 is : {head3}')
        if carry:
            head3.next = ListNode(carry)
        return top
            
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

aa = Solution()
print(aa.addTwoNumbers(l1, l2))
# print(aa.addTwoNumbers(l1, l2).next.val)