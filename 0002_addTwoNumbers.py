# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node_l1 = l1
        node_l2 = l2

        summation = (node_l1.val + node_l2.val) % 10
        carry = (node_l1.val + node_l2.val) // 10
        
        result_head = ListNode(summation)
        result_last = result_head

        while (node_l1.next or node_l2.next):

            summation = 0
            if node_l1.next:
                node_l1 = node_l1.next
                summation += node_l1.val
            if node_l2.next:
                node_l2 = node_l2.next
                summation += node_l2.val

            result_last.next = ListNode((summation + carry) % 10)
            carry = (summation + carry) // 10
            result_last = result_last.next

        
        if carry:
            result_last.next = ListNode(carry)
        
        return result_head
