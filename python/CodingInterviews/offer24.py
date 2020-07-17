'''
Function:
    反转链表
Author:
    Charles
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(prev, head):
            if not head: return prev
            next = head.next
            head.next = prev
            head, prev = next, head
            return recur(prev, head)
        return recur(None, head)