'''
Function:
    归并排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''数组合并'''
def Merge(array_1, array_2):
    result = []
    while array_1 and array_2:
        if array_1[0] < array_2[0]:
            result.append(array_1.pop(0))
        else:
            result.append(array_2.pop(0))
    if array_1:
        result += array_1
    if array_2:
        result += array_2
    return result


'''归并排序'''
def MergeSort(array):
    if len(array) < 2: return array
    pointer = len(array) // 2
    left = array[:pointer]
    right = array[pointer:]
    return Merge(MergeSort(left), MergeSort(right))


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = MergeSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))