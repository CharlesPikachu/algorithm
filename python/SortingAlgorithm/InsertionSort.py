'''
Function:
    插入排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''插入排序'''
def InsertionSort(array):
    length = len(array)
    for i in range(1, length):
        pointer, cur = i - 1, array[i]
        while pointer >= 0 and array[pointer] > cur:
            array[pointer+1] = array[pointer]
            pointer -= 1
        array[pointer+1] = cur
    return array


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = InsertionSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))