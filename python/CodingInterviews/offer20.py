'''
Function:
    表示数值的字符串
Author:
    Charles
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4}, # 0. start with 'blank'
            {'d': 2, '.': 4} ,                # 1. 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8}, # 2. 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},         # 3. 'digit' after 'dot'
            {'d': 3},                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            {'s': 6, 'd': 7},                 # 5. 'e'
            {'d': 7},                         # 6. 'sign' after 'e'
            {'d': 7, ' ': 8},                 # 7. 'digit' after 'e'
            {' ': 8}                          # 8. end with 'blank'
        ]
        pointer = 0
        while s:
            c, s = s[0], s[1:]
            if c >= '0' and c <= '9': r = 'd'
            elif c in '+-': r = 's'
            elif c in 'eE': r = 'e'
            elif c in '.': r = '.'
            elif c in ' ': r = ' '
            else: r = 'none'
            if r not in states[pointer]: return False
            pointer = states[pointer][r]
        return pointer in [2, 3, 7, 8]