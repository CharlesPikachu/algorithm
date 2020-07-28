'''
Function:
    序列化二叉树
Author:
    Charles
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root: return '[]'
        nums, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                nums.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                nums.append('null')
        return '[' + ','.join(nums) + ']'
    def deserialize(self, data):
        if data == '[]': return
        data = data[1: -1].split(',')
        root = TreeNode(int(data[0]))
        queue, pointer = [root], 1
        while queue and pointer < len(data):
            node = queue.pop(0)
            if data[pointer] != 'null':
                node.left = TreeNode(int(data[pointer]))
                queue.append(node.left)
            pointer += 1
            if data[pointer] != 'null':
                node.right = TreeNode(int(data[pointer]))
                queue.append(node.right)
            pointer += 1
        return root