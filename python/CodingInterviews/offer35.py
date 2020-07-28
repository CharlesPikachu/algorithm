'''
Function:
    复杂链表的复制
Author:
    Charles
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        record = {}
        def dfs(head):
            if not head: return
            if head in record:
                return record[head]
            copy = Node(head.val)
            record[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        return dfs(head)