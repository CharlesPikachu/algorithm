'''
Function:
    选择排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''选择排序'''
def SelectionSort(array):
    length = len(array)
    for i in range(length-1):
        idx_min = i
        for j in range(i+1, length):
            if array[j] < array[idx_min]:
                idx_min = j
        array[i], array[idx_min] = array[idx_min], array[i]
    return array


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = SelectionSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))