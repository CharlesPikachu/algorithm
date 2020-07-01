'''
Function:
    快速排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''快速排序'''
def QuickSort(array, left, right):
    if left >= right:
        return array
    pivot, i, j = array[left], left, right
    while i < j:
        while i < j and array[j] >= pivot:
            j -= 1
        array[i] = array[j]
        while i < j and array[i] <= pivot:
            i += 1
        array[j] = array[i]
    array[j] = pivot
    QuickSort(array, left, i-1)
    QuickSort(array, left+1, right)
    return array


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = QuickSort(array.copy(), 0, len(array)-1)
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))