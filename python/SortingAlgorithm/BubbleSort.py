'''
Function:
    冒泡排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''冒泡排序'''
def BubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]: array[j+1], array[j] = array[j], array[j+1] 
    return array


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = BubbleSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))