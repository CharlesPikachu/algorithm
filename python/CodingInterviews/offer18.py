'''
Function:
    删除链表的节点
Author:
    Charles
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        if head.val == val: return head.next
        pre, now = head, head.next
        while now:
            if now.val == val:
                pre.next = now.next
                break
            pre, now = now, now.next
        return head