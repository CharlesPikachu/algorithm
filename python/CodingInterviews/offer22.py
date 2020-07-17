'''
Function:
    链表中倒数第k个节点
Author:
    Charles
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        n0, n1 = head, head
        for i in range(k): n1 = n1.next
        while n1:
            n0 = n0.next
            n1 = n1.next
        return n0